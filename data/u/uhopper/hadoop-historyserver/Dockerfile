FROM uhopper/hadoop:2.7.2  
ENV
YARN_CONF_yarn_timeline___service_leveldb___timeline___store_path=/hadoop/yarn/timeline  
RUN mkdir -p /hadoop/yarn/timeline  
VOLUME /hadoop/yarn/timeline  
  
ADD run.sh /run.sh  
RUN chmod a+x /run.sh  
  
CMD ["/run.sh"]  

