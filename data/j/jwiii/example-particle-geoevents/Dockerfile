FROM crunchydata/crunchy-postgres-gis:centos7-10.3-1.8.2  
ARG PG_MODE=primary  
ARG PG_DATABASE=postgres  
ARG PG_ROOT_PASSWORD=postgres  
ARG PG_PRIMARY_USER=postgres  
ARG PG_PRIMARY_PASSWORD=postgres  
ARG PG_USER=postgres  
ARG PG_PASSWORD=postgres  
ARG PG_PRIMARY_PORT=5432  
ENV PG_MODE=${PG_MODE}  
ENV PG_DATABASE=${PG_DATABASE}  
ENV PG_ROOT_PASSWORD=${PG_ROOT_PASSWORD}  
ENV PG_PRIMARY_USER=${PG_PRIMARY_USER}  
ENV PG_PRIMARY_PASSWORD=${PG_PRIMARY_PASSWORD}  
ENV PG_USER=${PG_USER}  
ENV PG_PASSWORD=${PG_PASSWORD}  
ENV PG_PRIMARY_PORT=${PG_PRIMARY_PORT}  
  
COPY ./*.sql ./one-script.sh /tmp/  
  
USER 0  
RUN /tmp/one-script.sh /opt/cpm/bin/setup.sql \  
&& cat /opt/cpm/bin/setup.sql  
  
USER 26  

