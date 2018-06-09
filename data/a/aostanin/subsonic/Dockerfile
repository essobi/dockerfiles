FROM alpine:3.4  
RUN apk --update add ffmpeg flac lame openjdk7-jre openssl && \  
mkdir /subsonic && \  
wget -qO-
http://prdownloads.sourceforge.net/subsonic/subsonic-5.3-standalone.tar.gz |
tar xzC /subsonic && \  
sed -i "s/ > \${LOG} 2>&1 &//" /subsonic/subsonic.sh # Don't fork  
  
ADD start.sh /start.sh  
  
VOLUME ["/data"]  
EXPOSE 4040  
CMD ["/start.sh"]  

