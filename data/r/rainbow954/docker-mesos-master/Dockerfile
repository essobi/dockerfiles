FROM registry.cn-hangzhou.aliyuncs.com/rainbow954/mesos:latest  
  
  
CMD ["mesos-master", "--registry=in_memory"]  
  
ENV MESOS_WORK_DIR /tmp/mesos  
  
VOLUME /tmp/mesos  
  
COPY entrypoint.sh /  
RUN chmod a+x /entrypoint.sh  
ENTRYPOINT ["/usr/local/bin/dumb-init", "/entrypoint.sh"]

