import json

class DataAnalyzer:
    def __init__(self):
        print("[Analyzer] Data Analyzer Module Loaded.")

    def analyze_text_log(self, log_data):
        """텍스트 로그를 분석하여 단어 수 및 키워드 추출 시뮬레이션"""
        print("[Analyzer] Analyzing log data...")
        word_count = len(log_data.split())
        has_error = "ERROR" in log_data.upper()
        
        report = {
            "status": "Success",
            "word_count": word_count,
            "contains_error_flag": has_error,
            "suggested_action": "Requires Claude LLM review" if has_error else "Clear"
        }
        return report

if __name__ == "__main__":
    analyzer = DataAnalyzer()
    sample_log = "[INFO] 2026-05-26: Task executed normally. No anomalies detected."
    print(json.dumps(analyzer.analyze_text_log(sample_log), indent=4))
