import os
from analyzer import DataAnalyzer
from file_manager import AutomationFileManager

class AIAutomationAgent:
    def __init__(self):
        self.api_key = os.getenv("ANTHROPIC_API_KEY")
        self.analyzer = DataAnalyzer()
        self.file_manager = AutomationFileManager()
        print("------------------------------------------")
        print("Initializing Advanced AI Automation Agent...")
        print("------------------------------------------")

    def run_pipeline(self, raw_data, output_filename):
        print(f"\n[Pipeline] Starting automation pipeline for: {output_filename}")
        
        # 1. 데이터 분석 모듈 작동
        analysis_result = self.analyzer.analyze_text_log(raw_data)
        
        # 2. Claude API 연동 체크 및 처리
        if not self.api_key:
            print("[System] Claude API key missing. Operating in local simulation mode.")
            final_content = f"Simulation Report:\nData Stats: {analysis_result}\n[Notice] Requesting Claude token to generate deep insights."
        else:
            print("[Claude AI] Generating deep insights based on analysis...")
            final_content = f"Claude Enhanced Report:\nOptimized execution path for stats: {analysis_result}"
        
        # 3. 파일 저장 자동화
        self.file_manager.save_report(output_filename, final_content)
        print("[Pipeline] Automation pipeline finished successfully.")

if __name__ == "__main__":
    agent = AIAutomationAgent()
    sample_data = "[ERROR] System structural mismatch found in engineering logic block."
    agent.run_pipeline(sample_data, "engineering_report.txt")
