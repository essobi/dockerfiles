FROM centos  
MAINTAINER chriscartydev@gmail.com  
  
# Set Catalina Path  
ENV CATALINA_HOME /opt/tomcat  
ENV PATH $CATALINA_HOME/bin:$PATH  
  
# Do the install of Java and TomCat  
RUN yum install -y wget && \  
wget --no-cookies --no-check-certificate --header "Cookie:
gpw_e24=http%3A%2F%2Fwww.oracle.com%2F; oraclelicense=accept-securebackup-
cookie" "http://download.oracle.com/otn-
pub/java/jdk/9.0.1+11/jdk-9.0.1_linux-x64_bin.rpm" && \  
yum install -y jdk-9.0.1_linux-x64_bin.rpm && rm jdk-9.0.1_linux-x64_bin.rpm
&& \  
wget http://apache.mirror.vexxhost.com/tomcat/tomcat-9/v9.0.2/bin/apache-
tomcat-9.0.2.tar.gz && \  
tar -zxpvf apache-tomcat-9.0.2.tar.gz -C /opt/ && \  
mv /opt/apache-tomcat-9.0.2 /opt/tomcat  
  
# Set workdir  
WORKDIR /opt/tomcat/bin/  
  
# Expose port and Run  
EXPOSE 8080  
CMD ["catalina.sh", "run"]  

