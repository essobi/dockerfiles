FROM java:8-jre  
  
MAINTAINER PalSzak  
  
RUN wget -q -O -
http://packages.confluent.io/archive/1.0/confluent-1.0.1-2.10.4.tar.gz | tar
-xzf - -C /opt  
  
ENV PATH /opt/confluent-1.0.1/bin:$PATH  
  
COPY docker-entrypoint.sh /docker-entrypoint.sh  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
COPY ./image/conf /opt/confluent-1.0.1/etc  
VOLUME ["/opt/confluent-1.0.1/etc"]  
  
EXPOSE 8082  
CMD ["kafka-rest-start", "/opt/confluent-1.0.1/etc/kafka-rest/kafka-
rest.properties"]  

