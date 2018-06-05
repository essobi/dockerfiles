FROM google/cloud-sdk:latest  
  
MAINTAINER nerd305@gmail.com  
  
RUN apt-get update && \  
apt-get install -y openssh-server jq && \  
mkdir /var/run/sshd && \  
sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin wihtout-password/'
/etc/ssh/sshd_config  
  
ADD init.sh /  
RUN chmod +x /init.sh  
  
# Clean up  
RUN apt-get autoremove -y && apt-get clean && rm -rf /var/lib/apt/lists/*
/tmp/* /var/tmp/*  
  
EXPOSE 22  
CMD ["/init.sh"]  

