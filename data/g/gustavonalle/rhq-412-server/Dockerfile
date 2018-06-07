FROM fedora  
MAINTAINER gustavonalle  
  
RUN (yum -y install supervisor unzip postgresql-server net-tools openssh-
server yum-utils java-1.7.0-openjdk-devel; \  
/usr/sbin/sshd-keygen; \  
yum -y autoremove; \  
yum clean all; \  
curl -L
"http://sourceforge.net/projects/rhq/files/latest/download?source=files" >
/usr/local/rhq.zip; \  
unzip /usr/local/rhq.zip && rm /usr/local/rhq.zip)  
  
ADD java_home.sh /root/.bashrc  
ADD java_home.sh /etc/profile.d/java_home.sh  
ADD start.ini /etc/supervisord.d/start.ini  
ADD setup.sh /root/setup.sh  
  
RUN echo "root:root" | chpasswd  
RUN sed -i -e 's/session required pam_loginuid.so/#session required
pam_loginuid.so/' /etc/pam.d/sshd  
  
RUN /root/setup.sh  
  
EXPOSE 22 7080 16163  
ENTRYPOINT ["/usr/bin/supervisord"]  

