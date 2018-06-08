FROM moremagic/centos:6.5  
MAINTAINER moremagic <itoumagic@gmail.com>  
  
RUN yum -y update && yum clean all  
RUN yum -y install wget; exit 0  
RUN yum -y install curl vim passwd openssh-server initscripts && yum clean all  
  
# ssh  
RUN ssh-keygen -t rsa -N "" -f /etc/ssh/ssh_host_rsa_key \  
&& ssh-keygen -t dsa -N "" -f /etc/ssh/ssh_host_dsa_key \  
&& pwconv \  
&& echo "root" | passwd --stdin root  
  
# Java8 install  
RUN wget --no-cookies --no-check-certificate --header "Cookie:
gpw_e24=http%3A%2F%2Fwww.oracle.com%2F; oraclelicense=accept-securebackup-
cookie" "http://download.oracle.com/otn-
pub/java/jdk/8u25-b17/jdk-8u25-linux-x64.rpm" -O jdk-8u25-linux-x64.rpm \  
&& rpm -ivh jdk-8u25-linux-x64.rpm \  
&& rm -f jdk-8u25-linux-x64.rpm  
  
# http-min-server  
ADD resource/ /opt/  
RUN chmod +x /opt/service.sh /opt/https-mini-server/run.sh  
  
EXPOSE 22 8443  
CMD /opt/service.sh  
  

