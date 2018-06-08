FROM centos:latest  
MAINTAINER david <david@cninone.com>  
  
RUN yum install -y epel-release && \  
yum update -y && \  
yum install -y passwd \  
openssh-server \  
openssh-clients \  
supervisor \  
initscripts && \  
yum clean all  
  
RUN mkdir /var/run/sshd  
RUN echo 'root:freego' | chpasswd  
RUN /usr/sbin/sshd-keygen  
RUN sed -i 's/#PermitRootLogin yes/PermitRootLogin yes/' /etc/ssh/sshd_config  
  
# SSH login fix. Otherwise user is kicked off after login  
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional
pam_loginuid.so@g' -i /etc/pam.d/sshd  
  
ENV NOTVISIBLE "in users profile"  
RUN echo "export VISIBLE=now" >> /etc/profile  
  
COPY supervisord.conf /etc/supervisord.d/supervisord.ini  
EXPOSE 22 80 443  
CMD ["/usr/bin/supervisord"]

