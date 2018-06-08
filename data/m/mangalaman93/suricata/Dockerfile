FROM ubuntu:latest  
MAINTAINER = Aman Mangal <amanmangal@gatech.edu>  
  
# install depedencies from standard repos  
RUN apt-get update && \  
apt-get install -y python-software-properties software-properties-common && \  
add-apt-repository ppa:oisf/suricata-stable -y && \  
apt-get update && \  
apt-get install -y suricata iptables  
  
# copy run script  
COPY run_suricata.sh /  
RUN chmod +x /run_suricata.sh  
  
# command to run snort  
CMD ["/bin/sh", "/run_suricata.sh"]  

