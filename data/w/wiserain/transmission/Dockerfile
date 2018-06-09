FROM linuxserver/transmission  
  
# install transmission web control  
ADD https://github.com/ronggang/transmission-web-
control/raw/master/release/install-tr-control.sh /tmp  
RUN cd /tmp && \  
echo -ne "1\n" | bash install-tr-control.sh && \  
rm install-tr-control.sh  
  
# install python, flexget, and other dependencies  
RUN apk add --no-cache python && \  
python -m ensurepip && \  
rm -r /usr/lib/python*/ensurepip && \  
pip install --upgrade pip setuptools && \  
  
apk add \--no-cache ca-certificates && \  
pip install --upgrade --force-reinstall --ignore-installed \  
transmissionrpc python-telegram-bot flexget && \  
rm -r /root/.cache  
  
# copy local files  
COPY root/ /  
  
# ports and volumes  
EXPOSE 9091 51413 3539  
VOLUME /config /downloads /watch /flexget  

