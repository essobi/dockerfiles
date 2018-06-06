FROM elek/hbase-base  
RUN apk update && apk add python && rm -rf /var/cache/apk/*  
ADD url .  
RUN wget `cat url` -O phoenix.tar.gz && tar zxf phoenix.tar.gz && rm
phoenix.tar.gz && mv apache-phoenix* phoenix  
RUN cp /opt/phoenix/*-server.jar /opt/hbase/lib/  

