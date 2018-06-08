FROM ubuntu:trusty  
MAINTAINER Ruben  
  
#USER root  
RUN apt-get update && apt-get install -y \  
openssh-server sudo  
# gen dummy keys, centos doesn't autogen them like ubuntu does  
RUN /usr/bin/ssh-keygen -A  
RUN sed -ri 's/^session\s+required\s+pam_loginuid.so$/session optional
pam_loginuid.so/' /etc/pam.d/sshd  
RUN useradd jenkins -m -s /bin/bash  
  
# Add public key for Jenkins login  
RUN mkdir /home/jenkins/.ssh  
#COPY /files/authorized_keys /home/jenkins/.ssh/authorized_keys  
RUN chown -R jenkins /home/jenkins  
RUN chgrp -R jenkins /home/jenkins  
#RUN chmod 600 /home/jenkins/.ssh/authorized_keys  
RUN chmod 700 /home/jenkins/.ssh  
  
# Add the jenkins user to sudoers  
RUN echo "jenkins ALL=(ALL) ALL" >> etc/sudoers  
  
#  
RUN mkdir /var/run/sshd  
RUN chmod 0755 /var/run/sshd  
  
#USER jenkins  
# Expose SSH port and run SSHD  
EXPOSE 22  
CMD ["/usr/sbin/sshd","-D"]  
#CMD ["sudo service ssh start"]  

