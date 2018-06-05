FROM centos:centos7  
MAINTAINER Ajeeth <ajeeth.samuel@gmail.com>  
  
RUN yum update -y  
RUN yum install -y wget && wget --no-check-certificate --no-cookies --header
"Cookie: oraclelicense=accept-securebackup-cookie"
http://download.oracle.com/otn-
pub/java/jdk/8u151-b12/e758a0de34e24606bca991d704f6dcbf/jdk-8u151-linux-x64.rpm  
RUN rpm -ivh jdk-8u151-linux-x64.rpm && rm jdk-8u151-linux-x64.rpm  
#RUN yum install -y wget && wget --no-check-certificate --no-cookies --header
"Cookie: oraclelicense=accept-securebackup-cookie"
http://download.oracle.com/otn-pub/java/jdk/7u79-b15/jdk-7u79-linux-x64.rpm  
#RUN rpm -ivh jdk-7u79-linux-x64.rpm && rm jdk-7u79-linux-x64.rpm  
RUN wget https://dl.fedoraproject.org/pub/epel/7/x86_64/Packages/e/epel-
release-7-11.noarch.rpm && rpm -ivh epel-release-7-*.rpm && rm epel-
release-7-*.rpm && yum install -y pwgen ca-certificates tar unzip && yum clean
all  
  
# Retrivieng Wren:DS 3.0.0 from Github  
RUN wget -O /opt/wrends.zip
https://github.com/WrenSecurity/wrends/releases/download/3.0.0/WrenDS-3.0.0.zip  
  
ENV LDAP_BASE_DN dc=example,dc=com  
ENV LDAP_ROOT_DN cn=Directory Manager  
ENV LDAP_ROOT_PASS changemefirst  
  
# Create the skeleton 1st run  
ADD scripts /scripts  
RUN chmod +x /scripts/*.sh && touch /first_run  
  
# Interface the environment  
#RUN mkdir /opt/wrends  
VOLUME /opt/wrends  
EXPOSE 1389 1636 4444  
# Kicking in  
CMD ["/scripts/start.sh"]  

