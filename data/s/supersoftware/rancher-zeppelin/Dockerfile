FROM supersoftware/rancher-spark  
  
# install zeppelin  
RUN cd /tmp \  
&& curl -LO
http://ftp.meisei-u.ac.jp/mirror/apache/dist/zeppelin/zeppelin-0.7.1/zeppelin-0.7.1-bin-
all.tgz \  
&& tar zxf zeppelin-0.7.1-bin-all.tgz \  
&& mv zeppelin-0.7.1-bin-all /zeppelin \  
&& rm zeppelin-0.7.1-bin-all.tgz  
  
# environment  
ENV ZEPPELIN_PORT 8080  
ENV ZEPPELIN_HOME /zeppelin  
ENV ZEPPELIN_CONF_DIR $ZEPPELIN_HOME/conf  
ENV ZEPPELIN_NOTEBOOK_DIR $ZEPPELIN_HOME/notebook  
ENV ZEPPELIN_COMMIT v0.7.1  
WORKDIR $ZEPPELIN_HOME  
  
ENV JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64/jre  
ENV PATH=/app/bin:/app/sbin:/zeppelin/bin:$PATH  
ENV SPARK_HOME=/app  
  
# entry point  
COPY docker-entrypoint.sh /  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD ["idle"]  

