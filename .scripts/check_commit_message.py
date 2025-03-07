#!/usr/bin/env python
import re
import sys
import json
from pathlib import Path

def main():
    """
    メイン関数: コミットメッセージをチェックする
    """
    # コミットメッセージファイルを読み込む
    commit_msg_file = sys.argv[1]
    with open(commit_msg_file, 'r') as f:
        commit_msg = f.read()
    
    # .cz.jsonから設定を読み込む
    config_path = Path('.cz.json')
    with open(config_path, 'r') as f:
        config = json.load(f)
    
    # 設定から必要な情報を取得
    customize = config.get('commitizen', {}).get('customize', {})
    schema_pattern = customize.get('schema_pattern')
    example = customize.get('example')
    
    # コミットメッセージを行に分割
    lines = commit_msg.strip().split('\n')
    if not lines:
        print("エラー: コミットメッセージが空です")
        return 1
    
    # 先頭行を取得 (コミット要約行)
    first_line = lines[0]
    
    # 先頭行がパターンにマッチするかチェック
    if not re.match(schema_pattern, first_line):
        print("エラー: コミットメッセージが設定されたパターンに従っていません")
        print(f"パターン: {schema_pattern}")
        print(f"例: {example}")
        return 1
    
    # すべてのチェックが通過したらコミットを許可
    return 0

if __name__ == "__main__":
    sys.exit(main())