FROM tianon/centos:6.5  
MAINTAINER tushar.pokle@gmail.com  
  
RUN yum install -y squid  
ADD squid.conf /etc/squid/squid.conf  
# Make cache dirs  
RUN squid -z -F  
  
EXPOSE 3128  
# -X verbose debug logging  
# -N Don't run in daemon mode - important for docker  
CMD squid -N -X  
  

