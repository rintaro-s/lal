import openpyxl
import json

def excel_to_json(file_path):
    # Excelファイルを読み込む
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook.active

    data_list = []

    # A列とB列のデータを取得してJSON形式に変換
    for row in sheet.iter_rows(min_row=2, values_only=True):
        prompt, response = row
        if prompt and response:
            data_list.append({
                "prompt": prompt,
                "response": response
            })

    # JSONファイルに出力
    with open('data2.json', 'w', encoding='utf-8') as json_file:
        json.dump(data_list, json_file, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    excel_file_path = '1.xlsx'  # ここにExcelファイルのパスを指定
    excel_to_json(excel_file_path)
