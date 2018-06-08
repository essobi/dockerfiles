FROM isthari/hadoop-base:latest  
  
ENV JAVA_HOME /usr  
  
RUN mkdir -p /hadoop/datanode  
RUN mkdir -p /hadoop/namenode  
  
COPY hdfs-site.xml /root/hadoop/etc/hadoop/hdfs-site.xml  
COPY start-hdfs.sh /root  
RUN chmod u+x /root/start-hdfs.sh  
RUN adduser --system yarn  
RUN groupadd supergroup  
RUN usermod -a -G supergroup yarn  
  
#RUN cd root; ./hadoop/bin/hdfs namenode -format  
CMD /root/start-hdfs.sh  
  

