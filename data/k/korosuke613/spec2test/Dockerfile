# FROM でベースとなるイメージを指定  
FROM ubuntu:latest  
  
# 作者の指定  
MAINTAINER Futa HIRAKOBA  
  
# ワークディレクトリ  
WORKDIR ~/  
  
# 更新  
RUN apt update && apt -y upgrade  
  
# 必要なプログラムのインストール  
RUN apt install -y apt-file  
RUN apt install -y software-properties-common  
RUN apt install -y wget git  
  
# Python3のインストール  
RUN add-apt-repository -y ppa:jonathonf/python-3.6  
RUN apt -y update  
RUN apt install -y python3.6 python3.6-dev  
RUN wget https://bootstrap.pypa.io/get-pip.py  
RUN python3.6 get-pip.py  
  
# mecabのインストール  
RUN apt install -y make xz-utils  
RUN apt install -y mecab libmecab-dev mecab-ipadic-utf8 -y  
RUN git clone \--depth 1 https://github.com/neologd/mecab-ipadic-neologd.git  
RUN yes no | mecab-ipadic-neologd/bin/install-mecab-ipadic-neologd -n  
  
# リポジトリのクローン  
WORKDIR ..  
RUN git clone https://github.com/korosuke613/spec2test.git ~/spec2test  
  
# Pythonライブラリのインストール  
RUN apt install -y gcc g++  
WORKDIR spec2test/  
RUN pwd  
RUN pip3 install -r ~/spec2test/requirements.txt  
  
# ロケールを日本に設定  
RUN apt install -y language-pack-ja  
RUN locale-gen ja_JP.UTF-8  
ENV LANG ja_JP.UTF-8  
ENV LANGUAGE ja_JP:en  
ENV LC_ALL ja_JP.UTF-8  
RUN ln -fs /usr/share/zoneinfo/Asia/Tokyo /etc/localtime  
  
# ログイン場所の追記  
RUN echo "cd ~/" >> ~/.bashrc

