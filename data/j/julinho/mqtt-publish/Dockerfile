FROM debian:jessie-slim  
  
ARG BUILD_DATE  
ARG VCS_REF  
LABEL maintainer="thia.mdossantos@gmail.com" \  
org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.name="Julinho IFSC: mqtt-publish" \  
org.label-schema.description="Script para publicar dados no mqtt" \  
org.label-schema.license="MIT" \  
org.label-schema.url="https://marvietech.com.br/" \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.vcs-url="https://github.com/julinho-ifsc/mqtt-publish" \  
org.label-schema.vendor="Marvi•E Technologies" \  
org.label-schema.version="3.6" \  
org.label-schema.schema-version="1.0"  
  
RUN apt-get update && \  
apt-get -y install mosquitto-clients  
  
COPY docker-entrypoint.sh /  
  
RUN chmod 0755 /docker-entrypoint.sh && \  
groupadd mqtt && \  
useradd -g mqtt -d /mqtt -m -s /bin/false mqtt && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
COPY main.sh /mqtt  
  
WORKDIR "/mqtt"  
USER "mqtt"  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD ["/bin/bash", "main.sh"]  

