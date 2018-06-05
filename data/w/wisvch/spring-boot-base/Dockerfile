FROM wisvch/openjdk:8-jre-slim  
  
RUN groupadd -r spring-boot \--gid=999 && useradd --no-log-init -r -g spring-
boot \--uid=999 spring-boot  
USER 999  
COPY docker-entrypoint.sh /usr/local/bin/  
ENTRYPOINT ["docker-entrypoint.sh"]  
WORKDIR /srv  
EXPOSE 8080  

