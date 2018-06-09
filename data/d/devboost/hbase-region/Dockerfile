FROM devboost/hadoop-base  
RUN apt-get install -y hbase-regionserver  
  
ADD http://ftp-stud.hs-
esslingen.de/pub/Mirrors/ftp.apache.org/dist/phoenix/phoenix-4.6.0-HBase-1.0/bin/phoenix-4.6.0-HBase-1.0-bin.tar.gz
/tmp/phoenix.tar.gz  
RUN mkdir /tmp/phoenix  
RUN tar xzfv /tmp/phoenix.tar.gz --strip 1 -C /tmp/phoenix  
RUN cp /tmp/phoenix/phoenix-4.6.0-HBase-1.0-server.jar /usr/lib/hbase/lib/  
RUN rm -r /tmp/phoenix/  
RUN rm /tmp/phoenix.tar.gz  
  
ADD hbase-site.xml /etc/hbase/conf/hbase-site.xml  
  
CMD ["hbase", "regionserver", "start"]  
  
EXPOSE 60020  
EXPOSE 60030  

