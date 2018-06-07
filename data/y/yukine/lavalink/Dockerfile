FROM openjdk:10-jre-slim  
  
LABEL name "Lavalink"  
LABEL version "2.0.0"  
LABEL maintainer "Yukine <DevYukine@gmx.de>"  
  
WORKDIR /opt/Lavalink  
  
RUN apt-get update \  
&& apt-get install -y curl  
  
RUN curl -o Lavalink.jar
https://ci.fredboat.com/repository/download/Lavalink_Build/3919:id/Lavalink.jar?guest=1  
  
ENV SERVER_PORT=2333 \  
SERVER_ADDRESS=0.0.0.0 \  
LAVALINK_SERVER_PASSWORD=12345 \  
LAVALINK_SERVER_WS_PORT=8080 \  
LAVALINK_SERVER_WS_HOST=0.0.0.0 \  
LAVALINK_SERVER_SOURCES_YOUTUBE=true \  
LAVALINK_SERVER_SOURCES_BANDCAMP=true \  
LAVALINK_SERVER_SOURCES_SOUNDCLOUD=true \  
LAVALINK_SERVER_SOURCES_TWITCH=true \  
LAVALINK_SERVER_SOURCES_VIMEO=true \  
LAVALINK_SERVER_SOURCES_MIXER=true \  
LAVALINK_SERVER_SOURCES_HTTP=true \  
LAVALINK_SERVER_SOURCES_LOCAL=false \  
LAVALINK_SERVER_SENTRY_DNS= \  
LAVALINK_SERVER_BUFFER_DURATION_MS=400 \  
LAVALINK_SERVER_YOUTUBE_PLAYLIST_LOAD_LIMIT=600  
CMD ["java", "-jar", "Lavalink.jar"]  

