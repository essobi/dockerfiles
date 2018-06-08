FROM jplock/zookeeper:latest  
  
ENV ZOOKEEPER_VERSION latest  
  
COPY run.sh /run.sh  
RUN chmod a+x /run.sh && \  
cp -Rv /opt/zookeeper/conf /opt/zookeeper/conf-dist && \  
echo "autopurge.snapRetainCount=3" >> /opt/zookeeper/conf-dist/zoo.cfg && \  
echo "autopurge.snapRetainCount=3" >> /opt/zookeeper/conf-dist/zoo_sample.cfg
&& \  
echo "autopurge.purgeInterval=1" >> /opt/zookeeper/conf-dist/zoo.cfg && \  
echo "autopurge.purgeInterval=1" >> /opt/zookeeper/conf-dist/zoo_sample.cfg &&
\  
/usr/bin/md5sum /opt/zookeeper/conf/zoo.cfg > /opt/zookeeper/conf-
dist/default-zoo.cfg.md5  
  
  
ENTRYPOINT ["/bin/bash"]  
CMD ["/run.sh"]  
  

