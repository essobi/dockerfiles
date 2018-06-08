FROM easypi/shadowsocks-libev  
RUN set -ex \  
&& apk add --no-cache ca-certificates supervisor python py-pip \  
&& update-ca-certificates \  
&& apk add --no-cache --virtual .TMP wget \  
&& wget -O /root/kcptun-linux-amd64.tar.gz
https://github.com/xtaci/kcptun/releases/download/v20170218/kcptun-linux-
amd64-20170218.tar.gz \  
&& mkdir -p /opt/kcptun \  
&& cd /opt/kcptun \  
&& tar xvfz /root/kcptun-linux-amd64.tar.gz \  
&& rm /root/kcptun-linux-amd64.tar.gz \  
&& apk del --virtual .TMP \  
&& pip install supervisor-stdout  
COPY supervisord.conf /etc/supervisord.conf  
ENV KCP_MTU=1350 KCP_MODE=fast KCP_KEY=123456789 KCP_DATASHARED=10
KCP_PARITYSHARED=3 KCP_SNDWND=128  
ENV TIMEOUT 3600  
EXPOSE 41111/udp  
  
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisord.conf"]  

