FROM openjdk:8-slim  
  
  
RUN apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y curl ca-certificates git
\  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
ENV CEREBRO_VERSION 0.7.3  
RUN cd /opt/ \  
&& curl -L -o cerebro-${CEREBRO_VERSION}.tgz
https://github.com/lmenezes/cerebro/releases/download/v${CEREBRO_VERSION}/cerebro-${CEREBRO_VERSION}.tgz
\  
&& tar zxvf cerebro-${CEREBRO_VERSION}.tgz \  
&& rm cerebro-${CEREBRO_VERSION}.tgz \  
&& mkdir cerebro-${CEREBRO_VERSION}/logs \  
&& mv cerebro-${CEREBRO_VERSION} cerebro  
  
WORKDIR /opt/cerebro  
EXPOSE 9000  
COPY application.conf /opt/cerebro/conf/application.conf  
COPY docker-entrypoint.sh /docker-entrypoint.sh  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD ["./bin/cerebro"]  

