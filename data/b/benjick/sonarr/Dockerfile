FROM gliderlabs/alpine:3.3  
RUN echo "@testing http://nl.alpinelinux.org/alpine/edge/testing" >>
/etc/apk/repositories  
RUN apk add --no-cache \  
mono@testing \  
libmediainfo@testing \  
sqlite  
  
EXPOSE 8989  
VOLUME /volumes/config  
  
RUN curl -o sonarr.tar.gz -SL
http://update.sonarr.tv/v2/master/mono/NzbDrone.master.tar.gz \  
&& tar -xzf sonarr.tar.gz && rm sonarr.tar.gz  
  
CMD mono --debug NzbDrone/NzbDrone.exe --no-browser
-data=/volumes/config/sonarr  

