FROM healthcatalyst/fabric.baseos:latest  
  
LABEL maintainer="Health Catalyst"  
LABEL version="1.0"  
  
RUN yum -y update \  
&& yum -y install openssl \  
&& mkdir -p /opt/healthcatalyst/testca \  
&& yum -y install dos2unix \  
&& mkdir -p /opt/healthcatalyst/testca/certs \  
&& mkdir -p /opt/healthcatalyst/testca/private \  
&& chmod 700 /opt/healthcatalyst/testca/private \  
&& echo 01 > /opt/healthcatalyst/testca/serial \  
&& touch /opt/healthcatalyst/testca/index.txt  
  
COPY scripts /opt/healthcatalyst/  
  
ADD docker-entrypoint.sh ./docker-entrypoint.sh  
  
RUN mkdir -p /opt/healthcatalyst/server \  
&& mkdir -p /opt/healthcatalyst/client \  
&& dos2unix /opt/healthcatalyst/setupca.sh \  
&& chmod +x /opt/healthcatalyst/setupca.sh \  
&& dos2unix /opt/healthcatalyst/generateservercert.sh \  
&& chmod +x /opt/healthcatalyst/generateservercert.sh \  
&& dos2unix /opt/healthcatalyst/generateclientcert.sh \  
&& chmod +x /opt/healthcatalyst/generateclientcert.sh \  
&& dos2unix /opt/healthcatalyst/generatecerts.sh \  
&& chmod +x /opt/healthcatalyst/generatecerts.sh \  
&& dos2unix ./docker-entrypoint.sh \  
&& chmod +x ./docker-entrypoint.sh  
  
COPY openssl.cnf /opt/healthcatalyst/testca  
  
RUN mkdir -p /app && mkdir -p /app/public  
  
RUN curl --silent --location https://rpm.nodesource.com/setup_8.x | bash - \  
&& yum -y install nodejs  
  
ADD package.json /app/package.json  
ADD mini-webserver.js /app/mini-webserver.js  
  
RUN cd /app && npm install  
  
VOLUME ["/app/public"]  
  
EXPOSE 3000  
  
CMD ["node", "/app/mini-webserver.js"]  
  
ENTRYPOINT [ "./docker-entrypoint.sh" ]

