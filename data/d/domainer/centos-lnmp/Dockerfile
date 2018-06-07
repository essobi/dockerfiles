FROM centos:6  
MAINTAINER domainer  
  
# patch the system  
RUN yum clean all  
RUN yum -y update  
  
# set timezone to PRC  
RUN mv /etc/localtime /etc/localtime.bak  
RUN ln -s /usr/share/zoneinfo/Asia/Shanghai /etc/localtime  
  
# install NTP  
RUN yum -y install ntp  
RUN service ntpd start  
RUN chkconfig ntpd on  
  
# install epel  
RUN rpm -Uvh http://dl.fedoraproject.org/pub/epel/6/x86_64/epel-
release-6-8.noarch.rpm  
  
# install nginx  
RUN yum -y install nginx  
RUN service nginx start  
RUN chkconfig nginx on  
  
# install php  
RUN yum -y install php-fpm php-cli php-pdo php-mysql php-gd php-imap php-ldap
php-odbc php-pear php-xml php-xmlrpc php-mbstring php-mcrypt php-bcmath php-
mhash libmcrypt  
RUN chkconfig php-fpm on  
  
# install mysql  
RUN yum -y install mysql mysql-server  
RUN echo "NETWORKING=yes" > /etc/sysconfig/network  
# start mysqld to create initial tables  
RUN service mysqld start  
  
# install vim  
RUN yum -y install vim-enhanced  
  
# install supervisord  
RUN yum -y install python-pip && pip install "pip>=1.4,<1.5" \--upgrade  
RUN pip install supervisor  
  
# install sshd  
RUN yum install -y openssh-server openssh-clients passwd  
  
RUN ssh-keygen -q -N "" -t dsa -f /etc/ssh/ssh_host_dsa_key && ssh-keygen -q
-N "" -t rsa -f /etc/ssh/ssh_host_rsa_key  
RUN sed -ri 's/UsePAM yes/UsePAM no/g' /etc/ssh/sshd_config && echo
'root:changeme' | chpasswd  
  
ADD supervisord.conf /etc/  
EXPOSE 22 80  
CMD ["supervisord", "-n"]  

