FROM centos:7  
RUN yum install -y java-1.7.0-openjdk-headless tar epel-release  
  
RUN yum install -y python-pip jq  
  
RUN pip install awscli  
  
# https://www.apache.org/mirrors/dist.html  
RUN curl -fL
http://apache.mirror.digitalpacific.com.au/zookeeper/stable/zookeeper-3.4.8.tar.gz
| tar xzf - -C /opt && \  
mv /opt/zookeeper-3.4.8 /opt/zookeeper && \  
mkdir /opt/zookeeper/data  
  
COPY entrypoint.sh /  
  
ENTRYPOINT ["/entrypoint.sh"]  
  
ENV PATH
/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/opt/zookeeper/bin  
  
CMD ["zkServer.sh", "start-foreground"]  

