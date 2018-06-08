FROM node:4.3.1  
ENV DEBIAN_FRONTEND noninteractive  
ENV NODE_ENV=production  
ENV GATEWAY_VERSION=v1.1.0  
ENV SERVICEMANAGER_VERSION=v0.0.1  
ENV WEBCONSOLE_VERSION=v0.0.9  
ENV R_VERSION=3.2.3-r0  
ENV ADDRESS=0.0.0.0  
ENV SEED_DB=true  
ENV MYSQL_USER=iot  
ENV MYSQL_PASSWORD=secret$1  
ENV MYSQL_DATABASE=IOTDB  
ENV MYSQL_HOST=localhost  
ENV MYSQL_PORT=3306  
ENV MYSQL_OPTIONS_POOL_MINCONNECTIONS=1  
ENV MYSQL_OPTIONS_POOL_MAXCONNECTIONS=10  
ENV TESTS_AUTH=true  
ENV TESTS_STATISTIC=false  
ENV TESTS_ZERO=false  
ENV STATISTICS_SIGMA=6  
ENV SERVICEMANAGER_URL=http://localhost:8000  
ENV TESTS_AUTH=true  
ENV TESTS_STATISTIC=false  
ENV TESTS_ZERO=false  
ENV STATISTICS_SIGMA=6  
RUN apt-get update && apt-get install -y mysql-server mysql-client curl r-base
r-base-dev figlet  
  
WORKDIR /app/  
RUN curl -o gateway-${GATEWAY_VERSION}.tar.gz -sSL https://github.com/meccano-
iot/gateway/releases/download/${GATEWAY_VERSION}/meccano-
gateway-${GATEWAY_VERSION}.tar.gz && \  
curl -o /schema.sql -sSL https://raw.githubusercontent.com/meccano-
iot/gateway/${GATEWAY_VERSION}/sql/schema.sql && \  
curl -o servicemanager-${SERVICEMANAGER_VERSION}.tar.gz -sSL
https://github.com/meccano-
iot/servicemanager/releases/download/${SERVICEMANAGER_VERSION}/meccano-
servicemanager-${SERVICEMANAGER_VERSION}.tar.gz && \  
curl -o webconsole-${WEBCONSOLE_VERSION}.tar.gz -sSL
https://github.com/meccano-
iot/webconsole/releases/download/${WEBCONSOLE_VERSION}/meccano-
webconsole-${WEBCONSOLE_VERSION}.tar.gz && \  
mkdir -p /app/gateway /app/servicemanager /app/webconsole && \  
tar -zxf gateway-${GATEWAY_VERSION}.tar.gz -C /app/gateway && \  
tar -zxf servicemanager-${SERVICEMANAGER_VERSION}.tar.gz -C
/app/servicemanager && \  
tar -zxf webconsole-${WEBCONSOLE_VERSION}.tar.gz -C /app/webconsole && \  
rm -f gateway-${GATEWAY_VERSION}.tar.gz
servicemanager-${SERVICEMANAGER_VERSION}.tar.gz
webconsole-${WEBCONSOLE_VERSION}.tar.gz /app/gateway/config/config.yml  
  
# Install RMySQL package  
RUN chmod a+x /app/servicemanager/plugins/packages.R  
RUN /app/servicemanager/plugins/packages.R  
  
RUN cd /app/gateway && npm install --prod > /dev/null && \  
cd /app/servicemanager && npm install --prod > /dev/null --prod && \  
cd /app/webconsole/dist && npm install --prod > /dev/null --prod  
  
COPY my.cnf /etc/mysql/my.cnf  
COPY mysql-startup.sh /mysql-startup.sh  
COPY entrypoint.sh /entrypoint.sh  
RUN chmod a+x /entrypoint.sh /mysql-startup.sh  
RUN /mysql-startup.sh  
  
# Expose ports.  
CMD /entrypoint.sh  
EXPOSE 9000 3000 8000  

