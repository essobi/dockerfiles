# Play framework v1.4  
# docker run --rm pottava/play:1.4  
  
FROM pottava/java:8  
  
RUN apk --no-cache add \--virtual build-dependencies curl unzip \  
&& apk --no-cache add python \  
&& curl --location -s https://downloads.typesafe.com/play/1.4.2/play-1.4.2.zip
> /tmp/play-1.4.2.zip \  
&& unzip -q /tmp/play-1.4.2.zip -d /opt \  
&& rm -rf /tmp/play-1.4.2.zip \  
/opt/play-1.4.2/COPYING \  
/opt/play-1.4.2/documentation \  
/opt/play-1.4.2/framework/test-src \  
/opt/play-1.4.2/play.bat \  
/opt/play-1.4.2/python/*.dll \  
/opt/play-1.4.2/python/python.* \  
/opt/play-1.4.2/README.textile \  
/opt/play-1.4.2/samples-and-tests \  
/opt/play-1.4.2/support \  
&& ln -sf /opt/play-1.4.2/play /usr/local/bin \  
&& ln -sf /opt/play-1.4.2 /play-1.4.2 \  
&& apk del --purge build-dependencies  
  
CMD ["play"]  

