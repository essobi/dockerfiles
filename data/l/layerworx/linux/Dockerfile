FROM amazonlinux:latest  
  
LABEL version="2017.09"  
LABEL description="Layerworx Linux Standard Base"  
LABEL maintainer="Steven Crothers <steven.crothers@layerworx.com>"  
  
ADD files/bash_profile /root/.bash_profile  
ADD files/bashrc /root/.bashrc  
ADD files/prompt.sh /etc/profile.d/prompt.sh  
  
WORKDIR /root  
  
CMD ["/bin/bash"]  

