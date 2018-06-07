FROM fedora  
MAINTAINER Alessandro Arrichiello "alezzandro@gmail.com"  
# Download the latest stable repository available  
RUN curl -s
http://download.opensuse.org/repositories/home:/kamailio:/v4.3.x-rpms/Fedora_21/home:kamailio:v4.3.x-rpms.repo
-o /etc/yum.repos.d/kamailio-latest.repo  
  
# Install all the kamailio packages (this will include all the modules)  
RUN yum install -y kamailio*  
  
# Expose the default SIP server port  
EXPOSE 5060  
# Set the default command to run when starting the container  
CMD ["/usr/sbin/kamailio", "-DD","-P", "/var/run/kamailio.pid", "-f",
"/etc/kamailio/kamailio.cfg"]  

