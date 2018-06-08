FROM openresty/openresty:1.11.2.5-jessie  
MAINTAINER QuantRocket <support@quantrocket.com>  
  
RUN echo "deb http://ftp.debian.org/debian jessie-backports main" >
/etc/apt/sources.list.d/jessie-backports.list \  
&& apt-get update && apt-get install -y \  
certbot -t jessie-backports  
  
ENV NOVNCVERSION=0.6.2  
RUN curl --fail --output /tmp/novnc.zip
https://codeload.github.com/novnc/noVNC/zip/v${NOVNCVERSION} \  
&& cd /tmp \  
&& unzip novnc.zip \  
&& mv noVNC-${NOVNCVERSION} /usr/local/openresty/nginx/html/novnc \  
&& rm novnc.zip  
  
COPY nginx /usr/local/openresty/nginx/  
COPY bin /opt/quantrocket/bin/  
RUN chmod +x /opt/quantrocket/bin/*  
  
EXPOSE 80 443  
ENTRYPOINT ["/bin/bash"]  
CMD ["/opt/quantrocket/bin/houston.sh"]  

