FROM python:3-alpine  
  
  
COPY shadowsocks.ini /etc/supervisor.d/shadowsocks.ini  
COPY run.sh /run.sh  
  
RUN \  
echo "@testing http://dl-4.alpinelinux.org/alpine/edge/testing" >>
/etc/apk/repositories && \  
apk add \--update py-m2crypto@testing py-gevent@testing supervisor && rm -rf
/var/cache/apk/* && \  
sed -i 's/^\\(\\[supervisord\\]\\)$/\1\nnodaemon=true/' /etc/supervisord.conf
&& \  
mkdir -p /var/log/supervisor/ && \  
pip install shadowsocks && \  
chmod 755 /run.sh  
  
EXPOSE 3108  
#CMD ["/run.sh"]  
ENTRYPOINT ["/bin/sh", "-c", "/run.sh"]  
  

