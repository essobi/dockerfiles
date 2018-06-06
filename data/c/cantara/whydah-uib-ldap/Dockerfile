FROM ubuntu:trusty  
MAINTAINER Kim Christian Gaarder <kim.christian.gaarder@gmail.com>  
  
RUN apt-get update  
  
# Tools  
RUN apt-get install -y curl  
RUN apt-get install -y wget  
RUN apt-get install -y unzip  
RUN apt-get install -y openssh-server  
RUN apt-get install -y ldap-server  
RUN apt-get install -y ldap-client  
RUN apt-get install -y ldap-utils  
RUN apt-get install -y supervisor  
  
# Configure sshd - should probably be fortified  
RUN mkdir -p /var/run/sshd  
RUN echo 'root:kjempehemmelig' | chpasswd  
RUN sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/'
/etc/ssh/sshd_config  
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional
pam_loginuid.so@g' -i /etc/pam.d/sshd  
RUN echo "export VISIBLE=now" >> /etc/profile  
#RUN /usr/bin/ssh-keygen  
EXPOSE 22  
# Configure supervisor  
RUN mkdir -p /var/log/supervisor  
EXPOSE 389  
# Add commands last to speed up rebuilds, these are part of sshd and
supervisor configuration  
ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
ADD init-ldap.sh /scripts/init-ldap.sh  
  
# Add VOLUMEs to allow backup of config, logs and databases  
# * To store the data outside the container, mount /var/lib/ldap as a data
volume  
VOLUME ["/etc/ldap", "/var/lib/ldap", "/run/slapd"]  
  
CMD ["/usr/bin/supervisord"]  

