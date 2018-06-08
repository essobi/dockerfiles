FROM jeanblanchard/tomcat:8  
ENV MADSONIC_VERSION="6.2" MADSONIC_BUILD="9080" MADSONIC_DATE="20161222"
LC_ALL="C.UTF-8" LANG="en_US.UTF-8" LANGUAGE="en_US.UTF-8" TZ="Europe/Berlin"
MAX_MEM="256"  
LABEL maintainer="Markus Birth <markus@birth-online.de>"  
LABEL version="${MADSONIC_VERSION}.${MADSONIC_BUILD}"  
LABEL description="Madsonic media streamer"  
LABEL org.label-schema.name="Madsonic" \  
org.label-schema.url="http://www.madsonic.org/" \  
org.label-schema.vcs-type="Git" \  
org.label-schema.vcs-url="https://github.com/mbirth/docker-madsonic"  
  
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
"http://madsonic.org/download/${MADSONIC_VERSION}/${MADSONIC_DATE}_madsonic-${MADSONIC_VERSION}.${MADSONIC_BUILD}-war-
tomcat.zip" \  
-O madsonic.war.zip \  
&& unzip madsonic.war.zip \  
&& rm madsonic.war.zip \  
&& mv madsonic.war ROOT.war \  
&& apk del tzdata \  
&& rm -rf /var/cache/*  
  
#ADD server.xml ${CATALINA_HOME}/conf/  
ENV JAVA_OPTS="-Xmx${MAX_MEM}m -Dmadsonic.host=0.0.0.0 -Dmadsonic.port=8080
-Dmadsonic.contextPath=/ -Dmadsonic.home=/data
-Dmadsonic.defaultMusicFolder=/music/
-Dmadsonic.defaultPodcastFolder=/podcasts/
-Dmadsonic.defaultPlaylistFolder=/playlists/ -Djava.awt.headless=true"  
VOLUME ["/data", "/music/", "/playlists/", "/podcasts/"]  
  
EXPOSE 8080  

