FROM jeanblanchard/tomcat:8  
ENV SUBSONIC_VERSION="6.1.3" LC_ALL="C.UTF-8" LANG="en_US.UTF-8"
LANGUAGE="en_US.UTF-8" TZ="Europe/Berlin" MAX_MEM="256"  
LABEL maintainer="Markus Birth <markus@birth-online.de>"  
LABEL version="$SUBSONIC_VERSION"  
LABEL description="Subsonic media streamer"  
LABEL org.label-schema.name="Subsonic" \  
org.label-schema.url="http://www.subsonic.org/" \  
org.label-schema.vcs-type="Git" \  
org.label-schema.vcs-url="https://github.com/mbirth/docker-subsonic"  
  
RUN apk upgrade -U \  
&& apk add ca-certificates openssl ffmpeg lame tzdata \  
&& cp /usr/share/zoneinfo/${TZ} /etc/localtime \  
&& echo "${TZ}" > /etc/timezone \  
&& mkdir -p /data/transcode /music/ /playlists/ /podcasts/ \  
&& ln -s /usr/bin/lame /data/transcode/lame \  
&& ln -s /usr/bin/ffmpeg /data/transcode/ffmpeg \  
&& cd ${CATALINA_HOME}/webapps/ \  
&& rm -rf ROOT \  
&& wget -q
"https://sourceforge.net/projects/subsonic/files/subsonic/$SUBSONIC_VERSION/subsonic-${SUBSONIC_VERSION}-war.zip"
\  
-O subsonic.war.zip \  
&& unzip subsonic.war.zip \  
&& rm subsonic.war.zip \  
&& mv subsonic.war ROOT.war \  
&& apk del tzdata \  
&& rm -rf /var/cache/*  
  
ADD server.xml ${CATALINA_HOME}/conf/  
ENV JAVA_OPTS="-Xmx${MAX_MEM}m -Dsubsonic.host=0.0.0.0
-Dsubsonic.contextPath=/ -Dsubsonic.home=/data
-Dsubsonic.defaultMusicFolder=/music/
-Dsubsonic.defaultPodcastFolder=/podcasts/
-Dsubsonic.defaultPlaylistFolder=/playlists/ -Djava.awt.headless=true"  
VOLUME ["/data", "/music/", "/playlists/", "/podcasts/"]  
  
EXPOSE 8080  

