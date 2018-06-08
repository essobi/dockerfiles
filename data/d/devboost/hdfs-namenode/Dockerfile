FROM devboost/hadoop-base  
RUN apt-get install -y hadoop-hdfs-namenode  
RUN cp -r /etc/hadoop/conf.empty /etc/hadoop/conf.final  
RUN update-alternatives --install /etc/hadoop/conf hadoop-conf
/etc/hadoop/conf.final 50  
RUN update-alternatives --set hadoop-conf /etc/hadoop/conf.final  
  
ADD core-site.xml /etc/hadoop/conf.final/core-site.xml  
ADD hdfs-site.xml /etc/hadoop/conf.final/hdfs-site.xml  
  
RUN hdfs namenode -format  
  
CMD hdfs namenode  
  
EXPOSE 9000  
EXPOSE 50010 50020 50070 50075 50090  

