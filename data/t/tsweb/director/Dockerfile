FROM tsweb/cron  
MAINTAINER Kazuhisa Kumagai <k-kumagai@ts.tv-osaka.co.jp>  
  
#--------------------------------------  
# install Ansible  
#--------------------------------------  
RUN rpm -ivh http://ftp.riken.jp/Linux/fedora/epel/6/x86_64/epel-
release-6-8.noarch.rpm  
RUN yum install -y ansible --enablerepo=epel  
  
#--------------------------------------  
# run  
#--------------------------------------  
ADD start.sh /start.sh  
RUN chmod +x /start.sh  
  
CMD ["/start.sh"]  

