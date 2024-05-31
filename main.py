import subprocess
import time


def start_module(module_path):
    return subprocess.Popen(module_path.split())


def main():
    aiogram_bot_path = "python aiogram_bot/bot.py"
    api_server_path = "python api_server/api.py"
    web_application_path = "node web_application/server.js"

    processes = {
        aiogram_bot_path: None,
        api_server_path: None,
        web_application_path: None
    }

    try:
        while True:
            for module_path, process in processes.items():
                if process is None or process.poll() is not None:
                    print(f"Запуск модуля: {module_path}")
                    processes[module_path] = start_module(module_path)

            # Проверяем статус процесса каждые 3 секунды
            time.sleep(3)
    except KeyboardInterrupt:
        print("Скрипт был прерван пользователем.")


if __name__ == "__main__":
    main()
