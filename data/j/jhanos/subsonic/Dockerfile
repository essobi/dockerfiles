FROM alpine  
RUN mkdir /downloads /subsonic && cd /downloads && wget
http://subsonic.org/download/subsonic-6.0-war.zip && unzip subsonic* && mv
subsonic.war /subsonic && rm -rf /downloads && cd / && apk --no-cache add
jetty-runner  
EXPOSE 8080  
CMD jetty-runner /subsonic/subsonic.war  

