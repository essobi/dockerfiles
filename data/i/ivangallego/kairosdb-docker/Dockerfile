FROM java:8-alpine  
LABEL maintainer="ivan.gallego.mateos@gmail.com"  
  
RUN apk upgrade libssl1.0 --update-cache && \  
apk add wget ca-certificates bash  
RUN wget -O /tmp/kairosdb-1.2.0-1.tar.gz \  
https://github.com/kairosdb/kairosdb/releases/download/v1.2.0/kairosdb-1.2.0-1.tar.gz  
  
RUN mkdir -p /opt/ && \  
cd /opt/ && \  
tar -xvf /tmp/kairosdb*  
  
EXPOSE 4242 8080 2003 2004  
ENV CASSANDRA_HOSTS cassandra  
  
ADD ./conf/kairosdb.properties /opt/kairosdb/conf/kairosdb.properties  
ADD run.sh /usr/bin/run.sh  
  
CMD ["/usr/bin/run.sh"]

