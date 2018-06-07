FROM debian:stretch  
MAINTAINER LWB  
  
# Signavio  
ENV MAJOR=10  
ENV VERSION=10.3.0  
ENV EXTERNAL_CONFIGURATION=/var/lib/signavio  
ENV WEBAPPS_PATH=/opt/tomcat/webapps  
ENV CONF_PATH=/opt/tomcat/conf.bak  
ENV LIB_PATH=/opt/tomcat/lib.bak  
ENV HOST=HOST  
ENV DB_URL=DB  
ENV DB_USERNAME=ADMIN  
ENV DB_PASSWORD=ADMIN  
ENV SMTP_HOST_NAME=HOST  
ENV SMTP_EMAIL=EMAIL  
ENV SMTP_PORT=25  
ENV SUPPORT_EMAIL=EMAIL  
  
ENV FILE_IMPORT_USER=ADMIN  
ENV FILE_IMPORT_PASSWORD=ADMIN  
ENV FILE_IMPORT_PATH=/  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get update && \  
apt-get install -y --force-yes --no-install-recommends cifs-utils unzip && \  
rm -rf /var/lib/apt/lists && \  
mkdir -p ${WEBAPPS_PATH} && \  
mkdir -p ${CONF_PATH} && \  
mkdir -p ${LIB_PATH}  
  
VOLUME ${WEBAPPS_PATH}  
VOLUME ${CONF_PATH}  
VOLUME ${LIB_PATH}  
  
COPY docker-entrypoint.sh /usr/local/bin/  
RUN ln -s usr/local/bin/docker-entrypoint.sh /entrypoint.sh # backwards compat  
RUN chmod +x /usr/local/bin/docker-entrypoint.sh  
ENTRYPOINT ["docker-entrypoint.sh"]

