from centos:6  
RUN yum -y update && yum -y install wget  
RUN wget
https://raw.githubusercontent.com/minepicco/dockerfiles/master/pingfederate/8.3.3/pf-
install.sh  
RUN chmod +x pf-install.sh  
CMD ["pf-install.sh -v 8.3.0"]  
ENTRYPOINT ["sh", "-c", "/home/pingfederate/bin/run.sh", "BACKGROUND"]  
  
EXPOSE 9999 9031 1099  

