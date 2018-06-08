FROM centos  
MAINTAINER Leonardo Souza <leonardosilva.souza@yahoo.com.br>  
  
RUN cd /opt/  
RUN yum -y install wget  
RUN wget --no-cookies --no-check-certificate --header "Cookie:
gpw_e24=http%3A%2F%2Fwww.oracle.com%2F; oraclelicense=accept-securebackup-
cookie" "http://download.oracle.com/otn-
pub/java/jdk/8u131-b11/d54c1d3a095b4ff2b6607d096fa80163/jdk-8u131-linux-x64.tar.gz"  
RUN tar xzf jdk-8u131-linux-x64.tar.gz  
RUN cd /jdk1.8.0_131/  
RUN alternatives --install /usr/bin/java java /opt/jdk1.8.0_131/bin/java 2  
RUN echo -e "1\n" | alternatives --config java  
RUN alternatives --install /usr/bin/jar jar /opt/jdk1.8.0_131/bin/jar 2  
RUN alternatives --install /usr/bin/javac javac /opt/jdk1.8.0_131/bin/javac 2  
RUN alternatives --set jar /opt/jdk1.8.0_131/bin/jar  
RUN alternatives --set javac /opt/jdk1.8.0_131/bin/javac  
RUN export JAVA_HOME=/opt/jdk1.8.0_131  
RUN export JRE_HOME=/opt/jdk1.8.0_131/jre  
RUN export PATH=$PATH:/opt/jdk1.8.0_131/bin:/opt/jdk1.8.0_131/jre/bin  
RUN cd /tmp/  
RUN wget https://s3-sa-east-1.amazonaws.com/bluesoft-
public/desafio/helloworld.jar  
  
RUN wget https://s3-sa-east-1.amazonaws.com/bluesoft-public/desafio/token.json  
  
RUN wget http://dl.fedoraproject.org/pub/epel/7/x86_64/e/epel-
release-7-10.noarch.rpm  
RUN rpm -ivh epel-release-7-10.noarch.rpm  
RUN yum -y install jq  
RUN keyjson=$(cat token.json | jq '.token')  
  
EXPOSE 8080  
CMD ["java -jar helloworld.jar -token=${keyjson}"]  

