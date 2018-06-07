FROM tomcat:7  
MAINTAINER lemon  
  
WORKDIR /root/  
  
RUN apt-get update && \  
apt-get install -yq --no-install-recommends wget pwgen ca-certificates && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
ADD create_tomcat_admin_user.sh /root/run/create_tomcat_admin_user.sh  
ADD run.sh /root/run/run_tomcat.sh  
  
RUN chmod +x /root/run/*.sh  
  
CMD ["/root/run/run_tomcat.sh"]  

