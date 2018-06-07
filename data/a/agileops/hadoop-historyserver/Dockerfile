FROM agileops/hadoop-base:2.9.1-0.9  
MAINTAINER michael@faille.io <michael@faille.io>  
  
HEALTHCHECK CMD curl -f http://localhost:8188/ || exit 1  
  
ENV
YARN_CONF_yarn_timeline___service_leveldb___timeline___store_path=/hadoop/yarn/timeline  
RUN mkdir -p /hadoop/yarn/timeline  
VOLUME /hadoop/yarn/timeline  
  
ADD run.sh /run.sh  
RUN chmod a+x /run.sh  
  
EXPOSE 8188  
CMD ["/run.sh"]  

