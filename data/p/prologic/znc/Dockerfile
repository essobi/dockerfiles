FROM alpine:latest  
MAINTAINER James Mills, prologic at shortcircuit dot net dot au  
  
RUN apk -U add build-base git openssl-dev && \  
apk -U add znc znc-dev znc-modperl znc-modtcl znc-modpython znc-extra && \  
apk -U add ca-certificates && \  
rm -rf /var/cache/apk/*  
  
RUN pip3 install requests  
  
ADD https://raw.githubusercontent.com/jpnurmi/znc-playback/master/playback.cpp
/usr/src/znc/modules/playback.cpp  
RUN znc-buildmod /usr/src/znc/modules/playback.cpp && \  
mv playback.so /usr/src/znc/modules/  
  
RUN cd /usr/src/znc/modules && git clone https://github.com/cocodelabs/znc-
palaver  
RUN cd /usr/src/znc/modules/znc-palaver && make && \  
mv palaver.so /usr/src/znc/modules/  
  
COPY mutter.py /usr/src/znc/modules/mutter.py  
COPY znc.conf /usr/src/configs/znc.conf  
COPY cert.pem /ssl/cert.pem  
COPY key.pem /ssl/key.pem  
  
ADD entrypoint.sh /entrypoint.sh  
  
VOLUME /ssl  
VOLUME /data  
  
EXPOSE 7000  
ENTRYPOINT ["/entrypoint.sh"]  
CMD []  

