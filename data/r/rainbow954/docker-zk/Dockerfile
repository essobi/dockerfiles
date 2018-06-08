FROM ubuntu:14.04  
MAINTAINER Peter Ericson <pdericson@gmail.com>  
  
RUN sed -i 's/archive.ubuntu.com/mirrors.ustc.edu.cn/g' /etc/apt/sources.list  
RUN apt-get update  
RUN apt-get -y upgrade  
RUN apt-get install -y openssh-server  
RUN apt-get install --no-install-recommends -y curl openjdk-7-jre-headless  
RUN apt-get install -y net-tools  
RUN service ssh start  
  
# https://github.com/Yelp/dumb-init  
RUN curl -fLsS -o /usr/local/bin/dumb-init https://github.com/Yelp/dumb-
init/releases/download/v1.0.2/dumb-init_1.0.2_amd64 && chmod +x
/usr/local/bin/dumb-init  
  
# https://www.apache.org/mirrors/dist.html  
RUN curl -fL
http://archive.apache.org/dist/zookeeper/zookeeper-3.4.8/zookeeper-3.4.8.tar.gz
| tar xzf - -C /opt && \  
mv /opt/zookeeper-3.4.8 /opt/zookeeper  
  
VOLUME /tmp/zookeeper  
  
COPY entrypoint.sh /  
COPY log4j.properties /opt/zookeeper/conf  
RUN chmod a+x /opt/zookeeper/conf/log4j.properties  
RUN chmod a+x /entrypoint.sh  
ENTRYPOINT ["/usr/local/bin/dumb-init", "/entrypoint.sh"]  
  
ENV PATH
/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/opt/zookeeper/bin  
  
# 添加测试用户admin，密码admin，并且将此用户添加到sudoers里  
RUN useradd admin  
RUN echo "admin:admin" | chpasswd  
RUN echo "admin ALL=(ALL) ALL" >> /etc/sudoers  
  
CMD ["zkServer.sh", "start-foreground"]  

