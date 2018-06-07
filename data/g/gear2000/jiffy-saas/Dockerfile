FROM gear2000/jiffy-base:16.04  
MAINTAINER Gary Leong <gwleong@gmail.com>  
############################################################  
#####Jiffy SaaS Pkgs - Private  
############################################################  
ADD install.sh /var/tmp/install.sh  
RUN /var/tmp/install.sh  
############################################################  
#####Initial Daemon  
############################################################  
CMD ["/opt/jiffy-saas/bin/run.py"]  

