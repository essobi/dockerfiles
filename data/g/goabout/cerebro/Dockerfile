FROM openjdk:8-jre  
  
MAINTAINER Go About <tech@goabout.com>  
  
ENV CEREBRO_VERSION=0.6.6 \  
ELASTICSEARCH_HOST=http://localhost:9200  
RUN cd /opt/ \  
&& wget -nv -O cerebro-${CEREBRO_VERSION}.tgz
https://github.com/lmenezes/cerebro/releases/download/v${CEREBRO_VERSION}/cerebro-${CEREBRO_VERSION}.tgz
\  
&& tar zxvf cerebro-${CEREBRO_VERSION}.tgz \  
&& rm cerebro-${CEREBRO_VERSION}.tgz \  
&& mkdir cerebro-${CEREBRO_VERSION}/logs  
  
WORKDIR /opt/cerebro-${CEREBRO_VERSION}  
EXPOSE 9000  
CMD ["sh", "-c", "exec bin/cerebro -Dhosts.0.host=$ELASTICSEARCH_HOST"]  

