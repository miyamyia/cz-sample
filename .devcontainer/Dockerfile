FROM node:18

# Pythonとpipxのインストール（Python 3.9以上を確保）
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-venv \
    python3-full \
    pipx \
    git \
    && rm -rf /var/lib/apt/lists/*

# pipxのパスを通してcommitizenをインストール
RUN pipx ensurepath && \
    pipx install commitizen && \
    pipx install pre-commit

# pnpmのインストール
RUN npm install -g pnpm

# TypeScript関連のグローバルパッケージ
RUN npm install -g typescript ts-node

# 環境変数の設定（pipxのパスを通す）
ENV PATH="/root/.local/bin:${PATH}"

# 作業ディレクトリの設定
WORKDIR /workspace
