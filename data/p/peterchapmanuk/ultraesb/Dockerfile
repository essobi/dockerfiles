FROM centos:latest  
MAINTAINER "peter.chapman@me.com"  
#Install Dependencies  
RUN yum -y install wget tar  
  
#Download and install Java 7 JDK  
RUN curl -L -C - -b "oraclelicense=accept-securebackup-cookie" -O
http://download.oracle.com/otn-pub/java/jdk/7u71-b14/jdk-7u71-linux-x64.rpm  
RUN rpm -Uhv jdk-7u71-linux-x64.rpm  
RUN alternatives --install /usr/bin/java java /usr/java/default/bin/java
999999 --slave /usr/bin/keytool keytool /usr/java/default/bin/keytool --slave
/usr/bin/rmiregistry rmiregistry /usr/java/default/bin/rmiregistry  
RUN alternatives --install /usr/bin/javac javac /usr/java/default/bin/javac
999999 --slave /usr/bin/jar jar /usr/java/default/bin/jar --slave
/usr/bin/rmic rmic /usr/java/default/bin/rmic  
  
#Delete Java 7 JDK RPM  
RUN rm -f jdk-7u71-linux-x64.rpm  
  
#Download and Install UltraESB Minimal  
RUN wget
http://downloads.adroitlogic.com/2.3.0/af63b414-9159-4a61-9ad1-ed069579ee7d/adroitlogic-
ultraesb-2.3.0-min.tar.gz  
RUN tar zxf adroitlogic-ultraesb-2.3.0-min.tar.gz -C /opt/  
  
#Delete UltraESB Tar file  
RUN rm -f adroitlogic-ultraesb-2.3.0-min.tar.gz  
  
#Set up environment variables  
RUN useradd ultraesb  
RUN echo "export JAVA_HOME=/usr/java/default/" > /etc/profile.d/java_home.sh  
RUN chown -R ultraesb /opt/ultraesb-2.3.0-min/  
  
USER ultraesb  
  
#Deploy custom config files  
COPY /ultraesb-2.3.0-min/conf/* /opt/ultraesb-2.3.0-min/conf/  
  
#Expose ports required for messaging  
EXPOSE 8280  
EXPOSE 8443  
#Expose ports required for JMX/RMI comms  
EXPOSE 1099  
EXPOSE 9994  
#Start the UltraESB daemon  
ENTRYPOINT ["/opt/ultraesb-2.3.0-min/bin/./ultraesb-daemon.sh", "console",
"-D", "FOREGROUND"]

