FROM centos/postgresql-94-centos7  
MAINTAINER Yugesh yugesh.a@tcs.com  
  
USER root  
  
# JDK INSTALLATION STARTS  
RUN yum update -y && \  
yum install -y wget && \  
wget --no-cookies --no-check-certificate --header "Cookie:
gpw_e24=http%3A%2F%2Fwww.oracle.com%2F; oraclelicense=accept-securebackup-
cookie" "http://download.oracle.com/otn-
pub/java/jdk/7u80-b15/jre-7u80-linux-x64.rpm" && \  
yum localinstall -y /jre-7u80-linux-x64.rpm && \  
rm -f /jre-7u80-linux-x64.rpm && \  
yum clean all  
  
# Set environment variables.  
ENV HOME /root  
  
# Define working directory.  
WORKDIR /root  
  
# JDK INSTALLATION ENDS  
EXPOSE 5432  
CMD ["/bin/bash", "/start_postgres.sh"]

