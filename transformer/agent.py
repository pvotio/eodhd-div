from datetime import datetime

import pandas as pd

from config import settings


class Agent:
    def __init__(self, data):
        self.data = data

    def transform(self):
        table_fields = {
            settings.OUTPUT_TABLE: [
                "date",
                "declarationDate",
                "recordDate",
                "paymentDate",
                "period",
                "value",
                "unadjustedValue",
                "currency",
            ],
        }

        result = {}

        for ticker, rows in self.data.items():
            if not rows:
                continue

            for table in table_fields:
                if not table in result:
                    result[table] = []

                for row in rows:

                    newrow = {
                        "bbg_comp_ticker": ticker,
                        "timestamp_created_utc": self.timenow(),
                    }
                    for k in table_fields[table]:

                        if "#" in k:
                            k, name = k.split("#")
                        else:
                            name = k

                        if k in row:
                            if row[k] != "NA":
                                if "date" in name.lower():
                                    newrow[name] = self.valcheck_date(row[k])
                                else:
                                    newrow[name] = self.valcheck(row[k])

                    if len(newrow) > 2:
                        result[table].append(newrow)

        for table in table_fields:
            result[table] = pd.DataFrame(result[table])
            
        return result

    @staticmethod
    def valcheck(value):
        if value in ["NA", "NaN", "", 0, "0", None]:
            return None
        
        elif isinstance(value, int):
            return round(float(value), 4)

        else:
            return value
        
    @staticmethod
    def valcheck_date(value):
        if value in ["NA", "NaN", "", 0, "0", None]:
            return None
        
        if "T" in value:
            value = value.split("T")[0]
        try:
            x = datetime.strptime(value, "%Y-%m-%d")
            if x.year < 1900:
                return None

            return value
        except Exception:
            return None

    @staticmethod
    def timenow():
        return datetime.utcnow()