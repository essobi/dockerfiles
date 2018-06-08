# rubyの2.3.6 をベースイメージに指定  
FROM ruby:2.3.6  
# ruby コンテナの中で実行するコマンドを以降に記載  
# rails 実行に必要な build-essentialとnodejsをインストール  
RUN apt-get update -qq && apt-get install -y build-essential nodejs  
  
# ruby コンテナのルートディレクトリにappディレクトリを作成  
RUN mkdir /app  
  
# appディレクトリを作業ディレクトリに指定  
WORKDIR /app  
  
# Dockerfileと同じディレクトリに存在するファイルをrubyコンテナのappディレクトリ配下にコピーする  
COPY Gemfile /app/Gemfile  
COPY Gemfile.lock /app/Gemfile.lock  
  
# Gemのインストールコマンド  
RUN bundle install  
  
# Dockerfileと同じディレクトリに存在するファイルをrubyコンテナ内にコピーする  
# 今後、作成していくスクリプトファイルや設定ファイルを含めたいため  
# (何回かビルドする予定)  
COPY . /app  

