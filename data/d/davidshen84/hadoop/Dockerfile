FROM openjdk:8-jre  
MAINTAINER Xi Shen <davidshen84@gmail.com>  
  
LABEL hadoop=2.7.3 jre=openjdk-8-jre  
  
RUN apt-get update && apt-get install -y \  
ssh  
ONBUILD COPY .ssh /root/.ssh  
  
ADD http://www-
us.apache.org/dist/hadoop/common/hadoop-2.7.3/hadoop-2.7.3.tar.gz /opt/  
RUN mkdir /opt/hadoop && \  
tar xzf /opt/hadoop-2.7.3.tar.gz --strip-components=1 -C /opt/hadoop && \  
rm /opt/hadoop-2.7.3.tar.gz  
  
COPY opt/ /opt  
COPY root/ /root  
  
EXPOSE \  
# dfs.namenode.http-address  
50070 \  
# yarn.resourcemanager.webapp.address  
8088 \  
# fs.defaultFS  
9000 \  
# mapreduce.jobhistory.webapp.address  
19888  
ENV HADOOP_PREFIX=/opt/hadoop  
VOLUME ["/data"]  
WORKDIR /opt/hadoop  
  
ENTRYPOINT ["/root/startup.sh"]  

