FROM java:8-jre-alpine  
ENV QUASAR_VER=26.1.1  
RUN apk add --update gettext openssl  
WORKDIR /usr/local/quasar  
COPY files .  
RUN chmod +x start.sh \  
&& wget -q -P quasar/files https://github.com/quasar-
analytics/quasar/releases/download/v${QUASAR_VER}/quasar-web-
assembly-${QUASAR_VER}.jar -O quasar-web-assembly.jar \  
&& wget -q -P quasar/files https://github.com/quasar-
analytics/quasar/releases/download/v${QUASAR_VER}/quasar-repl-
assembly-${QUASAR_VER}.jar -O quasar-repl-assembly.jar \  
&& wget -q -P quasar/files/plugins https://github.com/quasar-
analytics/quasar/releases/download/v${QUASAR_VER}/quasar-mongodb-internal-
assembly-${QUASAR_VER}.jar -O quasar-mongodb-internal-assembly.jar  
CMD [ "/usr/local/quasar/start.sh" ]  

