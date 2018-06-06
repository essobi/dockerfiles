FROM jimlintw/base:jdk-alpine  
  
RUN wget
http://ftp.mirror.tw/pub/apache/kafka/0.11.0.0/kafka_2.11-0.11.0.0.tgz && \  
tar -zxf kafka_2.11-0.11.0.0.tgz && \  
rm kafka_2.11-0.11.0.0.tgz && \  
ln -s /kafka_2.11-0.11.0.0 /kafka && \  
rm -rf /var/cache/apk/* /tmp/* /var/tmp/*  
  
COPY data /data  
COPY ENTRYPOINT.sh /ENTRYPOINT.sh  
  
RUN rm -rf /kafka/config && \  
ln -s /data/config /kafka/config  
  
ENTRYPOINT ["/ENTRYPOINT.sh"]  
CMD ["--version"]  

