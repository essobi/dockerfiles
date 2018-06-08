FROM openjdk:8-jre-alpine  
MAINTAINER yu zhao <nido.zhao@gmail.com>  
  
#prepare system  
RUN apk update \  
&& apk add ca-certificates wget \  
&& update-ca-certificates  
RUN apk add --update bash && rm -rf /var/cache/apk/*  
ENV HBASE_HOME=/hbase-0.98.12-hadoop2  
  
#download hbase  
RUN wget
https://archive.apache.org/dist/hbase/hbase-0.98.12/hbase-0.98.12-hadoop2-bin.tar.gz  
RUN tar -zxvf hbase-0.98.12-hadoop2-bin.tar.gz  
RUN rm hbase-0.98.12-hadoop2-bin.tar.gz  
  
#update hbase configuration  
COPY config/* /config/  
COPY config/hbase-site.xml ${HBASE_HOME}/conf  
COPY config/hbase-env.sh ${HBASE_HOME}/conf  
  
#start hbase in pseudo distributed mode  
COPY script/* /script/  
CMD /bin/bash /script/start-pseudo.sh && /bin/bash  

