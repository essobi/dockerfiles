FROM glassofwhiskey/liferay-portal:7.1-ce-b1  
LABEL maintainer="GlassOfWhiskey <iacopo.c92@gmail.com>"  
  
WORKDIR /usr/local  
  
ENV JMXREMOTE_PORT=9999  
ENV JPDA_TRANSPORT=dt_socket  
ENV JPDA_ADDRESS=8000  
RUN mkdir -p /tmp/themes \  
&& chown -R liferay:liferay /tmp/themes  
  
COPY ./configs/setenv.sh $CATALINA_HOME/bin/setenv.sh  
COPY ./configs/portal-docker.properties $CATALINA_HOME/webapps/ROOT/WEB-
INF/classes/portal-docker.properties  
  
EXPOSE 8000/tcp 9999/tcp 11311/tcp  
  
ENTRYPOINT ["catalina.sh", "jpda", "run"]

