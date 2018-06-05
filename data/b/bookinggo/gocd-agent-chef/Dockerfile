FROM gocd/gocd-agent-centos-7:v17.12.0  
WORKDIR /  
  
COPY terraform-entrypoint.sh /terraform-entrypoint.sh  
  
ENV GIT_SSH_KEY ''  
ENV GIT_KNOWN_HOST ''  
RUN chmod +x /terraform-entrypoint.sh  
RUN yum -y install wget gcc gcc-c++  
RUN wget
https://packages.chef.io/files/stable/chefdk/2.4.17/el/7/chefdk-2.4.17-1.el7.x86_64.rpm  
RUN rpm -Uvh /chefdk-2.4.17-1.el7.x86_64.rpm  
RUN rm -f /chefdk-2.4.17-1.el7.x86_64.rpm  
  
ENTRYPOINT ["/terraform-entrypoint.sh"]  

