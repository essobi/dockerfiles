FROM bytesized/base  
  
RUN apk --update add ffmpeg flac lame openjdk7-jre  
RUN mkdir /app  
RUN wget -qO-
http://prdownloads.sourceforge.net/subsonic/subsonic-6.0-standalone.tar.gz |
tar xzC /app  
  
COPY /static /  
  
VOLUME /data /config /media  
  
EXPOSE 4040  

