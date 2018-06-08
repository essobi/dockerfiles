FROM jetbrains/teamcity-server:latest  
LABEL maintainer="LolHens <pierrekisters@gmail.com>"  
  
ENV TINI_VERSION 0.16.1  
ENV TINI_URL
https://github.com/krallin/tini/releases/download/v$TINI_VERSION/tini  
  
  
ADD ["https://raw.githubusercontent.com/LolHens/docker-
tools/master/bin/cleanimage", "/usr/local/bin/"]  
RUN chmod +x "/usr/local/bin/cleanimage"  
  
RUN apt-get update \  
&& apt-get dist-upgrade -y \  
&& apt-get install -y \  
nano \  
&& cleanimage  
  
RUN curl -Lo "/usr/local/bin/tini" $TINI_URL \  
&& chmod +x "/usr/local/bin/tini"  
  
COPY ["bin/run-server.sh", "/run-server.sh"]  
RUN chmod +x "/run-server.sh"  
  
ENV TOMCAT_STOP_TIMEOUT 9  
ENTRYPOINT ["tini", "-g", "--"]  
CMD ["/run-services.sh"]  
  
VOLUME /data/teamcity_server/datadir  
VOLUME /opt/teamcity/logs  
  
EXPOSE 8111  

