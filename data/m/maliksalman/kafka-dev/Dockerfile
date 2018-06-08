FROM java  
  
LABEL maintainer="smalik@pivotal.io"  
  
WORKDIR /root/  
ADD http://ftp.wayne.edu/apache/kafka/1.1.0/kafka_2.11-1.1.0.tgz /root/  
RUN tar xzf *.tgz; rm *.tgz; ln -s $(ls) kafka  
  
ADD kafka-server-start.sh /root/  
RUN chmod 755 kafka-server-start.sh  
  
ENV ADVERTISED_HOST=""  
EXPOSE 9092 2181  
ENTRYPOINT /root/kafka-server-start.sh

