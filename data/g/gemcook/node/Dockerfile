# ベースイメージ  
FROM node:8.11.1-alpine  
  
ENV GLIB_VERSION 2.27-r0  
  
# 不足コマンドのインストール  
RUN apk update && \  
apk add --no-cache ca-certificates openssh make git wget  
  
# flow のインストール準備  
RUN update-ca-certificates && \  
wget -O /etc/apk/keys/sgerrand.rsa.pub
https://raw.githubusercontent.com/sgerrand/alpine-pkg-
glibc/master/sgerrand.rsa.pub && \  
wget "https://github.com/sgerrand/alpine-pkg-
glibc/releases/download/$GLIB_VERSION/glibc-$GLIB_VERSION.apk" && \  
apk add --no-cache "glibc-$GLIB_VERSION.apk" && \  
rm "glibc-$GLIB_VERSION.apk" && \  
yarn global add flow-bin && \  
flow version && \  
yarn global remove flow-bin  
  
# Pythonインストール  
# from frolvlad/alpine-python3  
RUN apk add --no-cache python3 && \  
python3 -m ensurepip && \  
rm -r /usr/lib/python*/ensurepip && \  
pip3 install --upgrade pip setuptools && \  
if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi && \  
if [[ ! -e /usr/bin/python ]]; then ln -sf /usr/bin/python3 /usr/bin/python;
fi && \  
rm -r /root/.cache  
  
# AWS CLIインストール  
RUN pip3 install awscli  
  
# 環境変数の設定  
# yarn global binのPATHを通す  
ENV TZ=Asia/Tokyo HOME=/home/node PATH=$PATH:/home/node/.yarn/bin  
  
# 一般ユーザに切り替え  
USER node  
WORKDIR $HOME  
  
# serverlessコマンド追加  
RUN yarn global add serverless  
  
CMD ["/bin/sh"]  

