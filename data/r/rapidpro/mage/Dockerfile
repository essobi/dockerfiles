FROM openjdk:8-jdk-alpine  
  
ENV MAGE_VERSION=0.1.82  
  
# make sure tar and openssl are up to date  
RUN set -ex \  
&& apk add \--no-cache openssl tar  
  
WORKDIR /mage  
  
RUN wget
"https://github.com/rapidpro/mage/releases/download/v$MAGE_VERSION/mage-$MAGE_VERSION-
bundle.tar.gz" && \  
tar -xvf mage-$MAGE_VERSION-bundle.tar.gz && \  
rm mage-$MAGE_VERSION-bundle.tar.gz  
  
ENV REDIS_HOST=localhost  
ENV REDIS_DATABASE=8  
ENV TEMBA_HOST=localhost:8000 TEMBA_AUTH_TOKEN=none  
ENV TWITTER_API_KEY=none TWITTER_API_SECRET=none  
ENV SEGMENTIO_WRITE_KEY=none  
ENV SENTRY_DSN=none  
ENV LIBRATO_EMAIL=none LIBRATO_API_TOKEN=none  
  
ENV STARTUP_CMD="java -jar mage.jar server config.yml"  
  
EXPOSE 8027 8028  
  
COPY stack/startup.sh /  
CMD ["/startup.sh"]  

