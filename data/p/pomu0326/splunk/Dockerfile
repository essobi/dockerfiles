FROM debian:wheezy  
MAINTAINER pomu0326@gmail.com  
  
ENV SPLUNK_VERSION 6.3.0  
ENV SPLUNK_BUILD aa7d4b1ccb80  
ENV SPLUNK_GROUP splunk  
ENV SPLUNK_USER splunk  
ENV SPLUNK_HOME /opt/splunk  
ENV SPLUNK_DATA_DIR /opt/data  
  
RUN apt-get update \  
&& apt-get install -y curl sudo \  
&& curl -L
http://download.splunk.com/products/splunk/releases/${SPLUNK_VERSION}/splunk/linux/splunk-${SPLUNK_VERSION}-${SPLUNK_BUILD}-Linux-x86_64.tgz
| tar zxvf - -C /opt \  
&& rm -rf /var/lib/apt/lists/*  
  
COPY ./scripts/entrypoint /opt/entrypoint  
RUN chmod +x /opt/entrypoint  
  
RUN groupadd ${SPLUNK_GROUP} \  
&& useradd -g ${SPLUNK_GROUP} -s /usr/sbin/nologin ${SPLUNK_USER}  
  
EXPOSE 8000 8089 8191  
VOLUME ["/opt/data"]  
ENTRYPOINT ["/opt/entrypoint"]  
CMD ["app:start"]  
  

