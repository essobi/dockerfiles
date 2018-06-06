FROM anapsix/alpine-java:8_jdk  
  
ENV CROWD_VER 2.8.4  
ENV CROWD_DATA /var/lib/atlassian/application-data/crowd  
  
RUN apk --update add curl \  
&& curl -LO
https://www.atlassian.com/software/crowd/downloads/binary/atlassian-
crowd-${CROWD_VER}.tar.gz \  
&& tar -xzf atlassian-crowd-${CROWD_VER}.tar.gz -C /usr/local \  
&& ln -s /usr/local/atlassian-crowd-${CROWD_VER} /usr/local/crowd \  
&& rm atlassian-crowd-${CROWD_VER}.tar.gz \  
&& apk --purge del curl  
  
RUN sed -i 's|#crowd.home=.*|crowd.home='"${CROWD_DATA}"'|g'
/usr/local/crowd/crowd-webapp/WEB-INF/classes/crowd-init.properties \  
&& sed -i 's|exec "$PRGDIR"/"$EXECUTABLE" start "$@"|exec
"$PRGDIR"/"$EXECUTABLE" run "$@"|g' /usr/local/crowd/apache-
tomcat/bin/startup.sh  
  
VOLUME /var/lib/atlassian/application-data  
EXPOSE 8095  
CMD '/usr/local/crowd/start_crowd.sh'  

