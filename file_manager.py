import os

class AutomationFileManager:
    def __init__(self, base_dir="./data"):
        self.base_dir = base_dir
        if not os.path.exists(self.base_dir):
            os.makedirs(self.base_dir)
            print(f"[FileManager] Created base directory: {self.base_dir}")

    def save_report(self, filename, content):
        """분석된 결과를 파일로 저장"""
        file_path = os.path.join(self.base_dir, filename)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"[FileManager] Report saved successfully to {file_path}")

    def list_pending_tasks(self):
        """처리해야 할 작업 파일 목록 가져오기"""
        return os.listdir(self.base_dir)

if __name__ == "__main__":
    fm = AutomationFileManager()
    fm.save_report("sample_report.txt", "Task Summary: All core systems operational.")
