import sys
# append the path of the parent directory
sys.path.append("..")
from core.data_manager import DataManager
import json


class QueryManager:

    def __init__(self, dm: DataManager) -> None:
        self.dm = dm
    
    def __del__(self):
        del self.dm
    
    def log_query(self, appguid: str, guid: str, original_query: str, rewritten_query: str, rewriting_path: list) -> None:
        self.dm.log_query(appguid, guid, original_query, rewritten_query, rewriting_path)
    
    def report_query(self, appguid: str, guid: str, query_time_ms: int) -> None:
        self.dm.report_query(appguid, guid, query_time_ms)

    def list_queries(self, user_id: str) -> list:
        queries = self.dm.list_queries(user_id)
        res = []
        for query in queries:
            res.append({
                'id': query[0],
                'timestamp': query[1],
                'rewritten': query[2],
                'before_latency': query[3],
                'after_latency': query[4],
                'sql': query[5],
                'suggestion': query[6],
                'suggested_latency': query[7],
                'app_name': query[8]
            })
        return res
    
    def rewriting_path(self, query_id: str) -> dict:
        original_sql = self.dm.get_original_sql(query_id)
        res = {
            "original_sql": original_sql,
            "rewritings":[]
        }
        rewritings = self.dm.list_rewritings(query_id)
        for rewriting in rewritings:
            res["rewritings"].append({
                "seq": rewriting[0],
                "rule": rewriting[1],
                "rewritten_sql": rewriting[2]
            })
        return res
