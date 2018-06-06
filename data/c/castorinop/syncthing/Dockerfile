FROM alpine  
  
RUN adduser -D user  
RUN mkdir -p /home/user/bin  
  
ENV SYNCTHING_VERSION 0.14.9  
ENV ARCH=amd64  
RUN apk add wget --update && \  
#FIXME check certificate  
wget --no-check-certificate
https://github.com/syncthing/syncthing/releases/download/v$SYNCTHING_VERSION/syncthing-
linux-$ARCH-v$SYNCTHING_VERSION.tar.gz -O sycnthing.tar.gz && \  
tar zxvf sycnthing.tar.gz && \  
mv syncthing-linux-$ARCH-v$SYNCTHING_VERSION/syncthing /home/user/bin/ && \  
rm sycnthing.tar.gz syncthing-linux-$ARCH-v$SYNCTHING_VERSION -r && \  
rm -rf /tmp/src && \  
rm -rf /var/cache/apk/*  
  
RUN chown user.user /home/user/bin -Rv  
  
COPY noarch/*.sh /usr/bin/  
RUN chmod 755 /usr/bin/*sh  
  
env PATH /home/user/bin:$PATH  
  
ENV APP_BIN=syncthing  
ENV APP_ARGS="-gui-address=0.0.0.0:8384"  
ENTRYPOINT ["entrypoint.sh"]  
  
EXPOSE 8384  
EXPOSE 22000  

