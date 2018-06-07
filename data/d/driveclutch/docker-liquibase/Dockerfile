FROM driveclutch/alpine-java:1.0  
USER root  
  
RUN echo "@edge http://nl.alpinelinux.org/alpine/edge/main" >>
/etc/apk/repositories && \  
apk update && \  
apk add curl "libpq@edge<9.7" "postgresql-client@edge<9.7" && \  
rm -rf /var/cache/apk/*  
  
COPY lib/* /tmp/  
  
RUN mkdir liquibase && \  
tar -xzf /tmp/liquibase-3.5.3-bin.tar.gz -C liquibase && \  
chmod +x liquibase/liquibase && \  
mkdir jdbc_drivers && \  
mv /tmp/postgresql-42.1.4.jar jdbc_drivers && \  
mkdir migrations  
  
WORKDIR migrations  
  
COPY update.sh /app  
  
CMD /app/update.sh  

