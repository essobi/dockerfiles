FROM rocker/rstudio:latest  
## This handle reaches Carl and Dirk  
MAINTAINER "Mark Yang" youngce0918@gmail.com  
#ENV http_proxy http://10.57.35.31:8080  
#ENV https_proxy https://10.57.35.31:8080  
##Install Java  
RUN wget --header "Cookie: oraclelicense=accept-securebackup-cookie"
http://download.oracle.com/otn-
pub/java/jdk/8u71-b15/jdk-8u71-linux-x64.tar.gz&&tar -xvzf
jdk-8u71-linux-x64.tar.gz&&mkdir -p /usr/local/java&&mv jdk1.8.0_71
/usr/local/java/jdk1.8.0_71  
RUN mv /etc/apt/apt.conf.d/default /tmp/default.bak&&apt-get update&&apt-get
install -y samba  
## evn var  
#RUN echo "#! /bin/sh\nexport SPARK_HOME=/usr/local/spark\nexport
HADOOP_HOME=/usr/local/hadoop\nexport
JAVA_HOME=/usr/local/java/jdk1.8.0_71\nexport
PATH=\$PATH:\$SPARK_HOME/bin:\$HADOOP_HOME/bin:\$JAVA_HOME/bin">>/etc/init.d/setEnv.sh&&chmod
755 /etc/init.d/setEnv.sh  
ENV SPARK_HOME /usr/local/spark  
ENV HADOOP_HOME /usr/local/hadoop  
ENV JAVA_HOME /usr/local/java/jdk1.8.0_71  
ENV PATH $PATH:$SPARK_HOME/bin:$HADOOP_HOME/bin:$JAVA_HOME/bin  
COPY userconf.sh /usr/bin/userconf.sh  
COPY createUser.sh /usr/bin/createUser.sh  
COPY .Rprofile /home/rstudio/.Rprofile  
#CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]  
CMD ["/init"]  

