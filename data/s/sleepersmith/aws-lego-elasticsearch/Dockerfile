FROM java:8  
ARG ES_TAR_NAME=elasticsearch-2.2.0  
ARG
ES_TAR_URL=https://download.elastic.co/elasticsearch/release/org/elasticsearch/distribution/tar/elasticsearch/2.2.0/  
EXPOSE 9200  
EXPOSE 9300  
# Create directory  
RUN mkdir /home/local  
WORKDIR /home/local  
  
# Download  
RUN wget ${ES_TAR_URL}${ES_TAR_NAME}.tar.gz && \  
tar --strip-components 1 -xvf ${ES_TAR_NAME}.tar.gz && \  
rm ${ES_TAR_NAME}.tar.gz  
  
# Install plugins  
RUN bin/plugin install cloud-aws && \  
bin/plugin install lmenezes/elasticsearch-kopf/v2.1.1 && \  
bin/plugin install royrusso/elasticsearch-HQ/v2.0.3  
  
# Add files  
ADD elasticsearch.yml ./config/  
ADD es-init.sh ./  
ADD limits.conf /etc/security/  
  
# Create user and assign permission  
RUN useradd -m elasticsearch && \  
chown -R elasticsearch /home/local && \  
chmod 777 /home/local/es-init.sh  
ENTRYPOINT ["/home/local/es-init.sh"]  

