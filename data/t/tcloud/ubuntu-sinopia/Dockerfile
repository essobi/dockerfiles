# Version 1.3  
FROM tcloud/ubuntu-node  
  
USER root  
  
ENV BASE_DIR=/opt/sinopia  
  
WORKDIR $BASE_DIR  
  
VOLUME ["/data","/log"]  
  
EXPOSE 4873  
ADD files/config.yaml ${BASE_DIR}/conf/config.yaml  
ADD files/htpasswd ${BASE_DIR}/conf/htpasswd  
  
RUN . /root/.nvm/nvm.sh && \  
npm install -g js-yaml sinopia sinopia-htpasswd && \  
npm cache clean && \  
mkdir -p /data/storage/cache && \  
chmod -R g+rw /data  
  
CMD ["sinopia", "-c", "/opt/sinopia/conf/config.yaml"]  
  
RUN echo "============> clean up...============>" && \  
DEBIAN_FRONTEND=noninteractive apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

