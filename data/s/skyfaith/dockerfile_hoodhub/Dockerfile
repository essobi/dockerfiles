FROM centos:centos7  
MAINTAINER DAVID-BOB  
  
ENV JVER 8  
ENV JUPD 101  
ENV JBUILD b13  
  
ENV JED ${JVER}u${JUPD}  
ENV JDK jdk1.${JVER}.0_${JUPD}  
  
RUN yum update -y  
RUN yum install -y \  
tar \  
wget  
  
RUN wget --no-cookies --no-check-certificate --header "Cookie:
gpw_e24=http%3A%2F%2Fwww.oracle.com%2F; oraclelicense=accept-securebackup-
cookie" "http://download.oracle.com/otn-
pub/java/jdk/${JED}-${JBUILD}/jdk-${JED}-linux-x64.tar.gz"  
RUN tar -xvf jdk-${JED}-linux-x64.tar.gz -C /opt && rm
jdk-${JED}-linux-x64.tar.gz  
  
RUN chown -R root: /opt/${JDK}  
RUN alternatives --install /usr/bin/java java /opt/${JDK}/bin/java 1  
RUN alternatives --install /usr/bin/javac javac /opt/${JDK}/bin/javac 1  
RUN alternatives --install /usr/bin/jar jar /opt/${JDK}/bin/jar 1  
  
#RUN yum install net-tools -y  
EXPOSE 8080  
RUN mkdir /home/hood  
#RUN cd /home/hood  
RUN wget
https://github.com/shiyang19822000/dockerfile_hoodhub/raw/master/hoodhub-0.0.1-SNAPSHOT.jar
-P /home/hood/  
#RUN nohup java -jar /home/hood/hoodhub-0.0.1-SNAPSHOT.jar >>
/home/hood/hoodhub.log &  
#RUN touch /home/hood/hoodhub.log  
#CMD ["nohup java -jar /home/hood/hoodhub-0.0.1-SNAPSHOT.jar >>
/home/hood/hoodhub.log &"]  
#RUN nohup java -jar /home/hood/hoodhub-0.0.1-SNAPSHOT.jar >
/home/hood/hoodhub.log 2>&1 &  
#RUN java -jar /home/hood/hoodhub-0.0.1-SNAPSHOT.jar  

