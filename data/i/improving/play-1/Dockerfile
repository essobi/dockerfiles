FROM improving/java  
  
ARG PLAY_VERSION="1.4.4"  
RUN apk update && apk add --no-cache wget python \  
&& cd /opt && wget --no-check-certificate
https://downloads.typesafe.com/play/${PLAY_VERSION}/play-${PLAY_VERSION}.zip \  
&& unzip -q play-${PLAY_VERSION}.zip && rm play-${PLAY_VERSION}.zip \  
&& ln -s /opt/play-${PLAY_VERSION} /opt/play \  
&& ln -s /opt/play/play /usr/local/bin/play \  
&& apk del wget  
  
ARG user=play  
RUN addgroup -g 1000 ${user} \  
&& adduser -h "/opt/app" -u 1000 -G ${user} -s /bin/bash -D ${user}  
  
COPY src/play-app.sh /opt/app/play-app.sh  
VOLUME "/opt/app/.ivy2"  
  
RUN chown -R ${user}:${user} /opt/app/  
USER ${user}  
  
WORKDIR /opt/app/run  
  
ENV APP_DIR="/opt/app/run"  
ENV JAVA_TIMEZONE=America/Sao_Paulo  
ENV MODE ""  
ENV DB_ADDRESS "<<localhost>>"  
ENV DB_NAME "diagnostico"  
ENV DB_USER "root"  
ENV DB_PASS "mysql"  
ENV PLAY_PROPERTIES=""  
EXPOSE 9000  
#Debug  
EXPOSE 8000  
CMD ["/opt/app/play-app.sh"]  
  
# docker build --force-rm -t improving-play-1 .  
# docker tag improving-play-1 improving/play-1  

