FROM manageiq/manageiq:latest  
MAINTAINER hawkular-dev@lists.jboss.org  
  
RUN yum -y install --setopt=tsflags=nodocs openssh-server &&\  
systemctl enable sshd  
  
RUN useradd -ou 0 -g 0 admin &&\  
echo "smartvm"|passwd admin --stdin  
  
EXPOSE 22 5432 80 443  

