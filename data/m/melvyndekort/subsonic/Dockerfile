FROM openjdk:8-jre-alpine  
  
RUN apk add --update --no-cache curl ffmpeg ffmpeg-libs  
  
RUN mkdir -p /opt/subsonic  
WORKDIR /opt/subsonic  
  
RUN curl -sL https://s3-eu-west-1.amazonaws.com/subsonic-
public/download/subsonic-6.1.3-standalone.tar.gz | tar xz \  
&& chmod -R u+rwX,go+rX,go-w /opt  
  
RUN mkdir -p /data /media \  
&& chmod 777 /data /media  
  
COPY startup.sh /  
  
EXPOSE 4040  
VOLUME ["/data", "/media"]  
  
CMD ["/startup.sh"]  
  

