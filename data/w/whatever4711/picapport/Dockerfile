FROM alpine:3.5  
LABEL authors "Marcel Großmann"  
LABEL maintainer "whatever4711@gmail.com"  
  
ENV PICAPPORT_PORT=80 \  
PICAPPORT_VERSION="v6.3.03"  
RUN apk add --update --no-cache openjdk8 curl && \  
mkdir -p /opt/picapport && \  
curl -SsL -o /opt/picapport/picapport-headless.jar
http://picapport.de/prepare_download_headless_jar-${PICAPPORT_VERSION}.php &&
\  
mkdir /opt/picapport/.picapport && \  
printf "%s\n%s\n%s\n" "server.port=$PICAPPORT_PORT"
"irobot.root.0.path=/srv/photos" "foto.jpg.usecache=2" >
/opt/picapport/.picapport/picapport.properties  
  
WORKDIR /opt/picapport  
EXPOSE ${PICAPPORT_PORT}  
  
#ENTRYPOINT ["java", "-DTRACE=INFO", "-Duser.home=/opt/picapport", "-cp",
"picapport.jar", "de.contecon.picapport.PicApport",
"-configfile=/opt/picapport/.picapport/picapport.properties",
"-pgui.enabled=false"]  
ENTRYPOINT ["java", "-Xms256m", "-Xmx512m", "-Duser.home=/opt/picapport",
"-jar", "picapport-headless.jar"]  

