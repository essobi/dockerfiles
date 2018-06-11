FROM dclong/spark:2.1.0-hdp2.7  
ARG version=0.7.2  
ARG zeppelin=zeppelin-${version}-bin-all  
ENV ZEPPELIN_HOME=/opt/$zeppelin  
  
RUN wget http://www-
us.apache.org/dist/zeppelin/zeppelin-${version}/$zeppelin.tgz -O
/tmp/zeppelin.tgz \  
&& tar -zxvf /tmp/zeppelin.tgz -C /opt/ \  
&& mkdir -p $ZEPPELIN_HOME/logs \  
&& mkdir -p $ZEPPELIN_HOME/run \  
&& mkdir -p /notebook \  
&& rm /tmp/zeppelin.tgz  
  
ADD zeppelin-env.sh /opt/$zeppelin/conf/  
EXPOSE 8080  
ENTRYPOINT ["sh", "-c", "$ZEPPELIN_HOME/bin/zeppelin.sh"]  

