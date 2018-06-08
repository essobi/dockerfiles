# Base on Fedora 20 image  
FROM jervine/fedora20  
  
MAINTAINER "Jonathan Ervine" <jon.ervine@gmail.com>  
ENV container docker  
  
# Install pre-requisites  
RUN yum update -y; yum clean all  
RUN yum install -y procps-ng util-linux openssh-server squid httpd-tools
supervisor; yum clean all  
  
# Install rutorrent  
RUN mkdir -p /var/run/sshd /var/run/supervisord  
RUN echo "root:password" | chpasswd  
RUN ssh-keygen -t rsa -f /etc/ssh/ssh_host_rsa_key -N ''  
RUN sed -i 's|session required pam_loginuid.so|session optional
pam_loginuid.so|g' /etc/pam.d/sshd  
  
RUN squid -z -F  
  
ADD squid.conf /etc/squid/squid.conf  
ADD supervisord.conf /etc/supervisord.conf  
  
EXPOSE 22  
EXPOSE 3128  
# Start processes  
ENTRYPOINT ["/bin/supervisord", "-n"]  

