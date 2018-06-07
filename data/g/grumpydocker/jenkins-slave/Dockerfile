FROM evarga/jenkins-slave  
MAINTAINER Alex Sherwin <alex.sherwin@gmail.com>  
  
RUN apt-get -y install sudo  
RUN adduser jenkins sudo  
RUN echo %sudo ALL=NOPASSWD: ALL >> /etc/sudoers  

