FROM ubuntu:latest  
  
LABEL maintainer="rajjoshi@comp.nus.edu.sg"  
  
# Install packages  
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y \  
apt-utils \  
locales \  
openssh-server \  
sudo  
RUN mkdir /var/run/sshd  
  
# To fix the locales  
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
# Do the user and ssh login setup  
COPY setup.sh /root  
COPY run.sh /root  
RUN chmod +x /root/*.sh  
  
EXPOSE 22  
EXPOSE 80  
CMD ["/root/run.sh"]

