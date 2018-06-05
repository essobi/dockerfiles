#The Base Images  
FROM centos:latest  
  
MAINTAINER Burgess Chen <loveshe76119@gmail.com>  
  
ENV SSH_PASSWORD=test123  
  
#install base tools  
RUN yum -y install dos2unix net-tools vixie-cron crontabs telnet screen wget
unzip tar vim  
  
#install ssh service  
RUN yum -y install openssh-server passwd  
#RUN sed -ri 's/#UsePAM no/UsePAM no/g' /etc/ssh/sshd_config && \  
RUN echo "${SSH_PASSWORD}" | passwd "root" \--stdin  
  
#Set Port  
EXPOSE 22  
#Copy init-bashrc.sh to Images  
COPY init-bashrc.sh /init-bashrc.sh  
RUN dos2unix /init-bashrc.sh  
RUN /usr/sbin/sshd-keygen -A  
  
# Create Base Enter Cont Command  
RUN chmod 755 /init-bashrc.sh && echo "/init-bashrc.sh" >> /root/.bashrc && \  
echo 'export PATH="/root/.composer/vendor/bin:$PATH"' >> /root/.bashrc  
  
# Start run shell  
CMD ["bash"]  
  

