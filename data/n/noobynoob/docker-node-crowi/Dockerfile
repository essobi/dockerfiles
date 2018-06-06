FROM node:4.5-slim  
MAINTAINER nooby  
  
ENV CROWI_VERSION v1.5.0  
# 以下の3ステップ構成でビルド  
# 一つのRUNコマンドで実行してるのは生成されるイメージを小さくするため  
#  
# 1. ビルドに必要なバイナリのインストール  
# RUN apt-get update && apt-get install -y \  
# git \  
# g++ \  
# make \  
# python \  
#  
# 2. crowiのクローンとビルド  
# && git clone -b $CROWI_VERSION https://github.com/crowi/crowi.git \  
# && cd /crowi \  
# && npm install --unsafe-perm \  
#  
# 3. 不要になったパッケージの削除  
# && apt-get autoremove -y \  
# && apt-get clean \  
# && rm -rf /var/lib/apt/lists/* \  
# && cd /crowi/node_modules && npm uninstall --save --unsafe-perm \  
# babel* \  
# gulp* \  
# webpack* \  
# && rm -rf \  
# /root/.npm \  
# /tmp/*  
RUN apt-get update && apt-get install -y \  
git \  
g++ \  
make \  
python \  
&& git clone -b $CROWI_VERSION https://github.com/crowi/crowi.git \  
&& cd /crowi \  
&& npm install --unsafe-perm \  
&& apt-get remove -y \  
git \  
g++ \  
make \  
python \  
&& apt-get autoremove -y \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* \  
&& cd /crowi/node_modules && npm uninstall --save --unsafe-perm \  
babel* \  
gulp* \  
webpack* \  
&& rm -rf \  
/root/.npm \  
/tmp/*  
  
ENV PORT ${PORT:-80}  
EXPOSE $PORT  
  
# timezoneをjstに  
# ref: https://serverfault.com/questions/683605/docker-container-time-
timezone-will-not-reflect-changes/683607  
ENV TZ=Asia/Tokyo  
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone  
  
WORKDIR /crowi  
COPY ./docker-entrypoint.sh /  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD ["npm", "start"]

