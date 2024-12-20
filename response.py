import json
import os

def create_json_data():
    data = []
    while True:
        prompt = input("プロンプト: ")
        if prompt.lower() == 'q':
            break

        response = input("レスポンス: ")
        data.append({"prompt": prompt, "response": response})

    return data

def save_json_data(data, filename="data.json"):
    try:
        if os.path.exists(filename):
            with open(filename, 'r', encoding='utf-8') as f:
                existing_data = json.load(f)
        else:
            existing_data = []

        existing_data.extend(data)

        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(existing_data, f, indent=2, ensure_ascii=False)
        print(f"{filename} に保存しました。")
    except json.JSONDecodeError:
        print(f"エラー: {filename} は正しいJSON形式ではありません。新しいデータのみ保存します。")
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print(f"{filename} に新しいデータを保存しました。")
    except Exception as e:
        print(f"エラーが発生しました: {e}")

if __name__ == "__main__":
    print("作成ツール")
    print("プロンプトとレスポンスを交互に入力してください。")
    print("終了する場合はプロンプトに 'q' を入力してください。")

    data = create_json_data()

    if data: # データが空でない場合のみ保存
        save_json_data(data)

    print("ありがとうございました。")
