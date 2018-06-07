FROM kalamangga/debian:jessie  
MAINTAINER Kalamangga.Net R&D  
RUN apt-get update && \  
apt-get install -y --force-yes openssh-server git gitweb && \  
apt-get clean -y  
ADD root.tar /root  
RUN /bin/bash /root/init.sh  
EXPOSE 80  
EXPOSE 22  
CMD ["/bin/bash","/root/service.sh"]  

