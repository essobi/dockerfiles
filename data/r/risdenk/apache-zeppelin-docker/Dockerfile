FROM openjdk:8-jre-alpine  
  
RUN apk --no-cache add bash  
  
RUN wget -qO-
http://ftp.wayne.edu/apache/zeppelin/zeppelin-0.7.2/zeppelin-0.7.2-bin-all.tgz
| tar zxv -C /  
RUN ln -nsf /zeppelin-* /zeppelin  
  
ADD entrypoint.sh /entrypoint.sh  
ENTRYPOINT /entrypoint.sh  
  

