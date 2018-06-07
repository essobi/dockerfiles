FROM alpine:3.5  
ENV APP_VERSION 0.5.1  
LABEL maintainer="tse.code@TossP.com" \  
version="0.0.1" \  
description="Decentralized websites using Bitcoin crypto and the BitTorrent
network - https://zeronet.io"  
  
RUN apk update && apk upgrade && \  
apk add \--no-cache python openssl wget\  
py-gevent py-msgpack py-setuptools \  
nodejs && \  
easy_install-2.7 Werkzeug && \  
npm i -g coffee-script && \  
wget -O f.zip --no-check-certificate
https://github.com/HelloZeroNet/ZeroNet/archive/v${APP_VERSION}.zip && \  
unzip f.zip && \  
mv ZeroNet-${APP_VERSION} app && \  
apk del wget && \  
rm -rf /var/cache/apk/* &&\  
rm f.zip &&\  
npm cache clean &&\  
mkdir -p /app/root/zeronet &&\  
ln -sv /root/zeronet/data/ /app/root/zeronet &&\  
echo -e "[global]\ndata_dir = /root/zeronet/data\nlog_dir = /root/zeronet/log"
> /etc/zeronet.conf  
  
VOLUME /root/zeronet  
  
EXPOSE 43110  
EXPOSE 15441  
ENTRYPOINT ["python", "/app/zeronet.py","--config_file","/etc/zeronet.conf","
--data_dir","/root/zeronet/data", "--log_dir","/root/zeronet/log", "--ui_ip",
"0.0.0.0"]  
CMD ["--debug"]  

