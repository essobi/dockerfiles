# Pull base image.  
FROM garland/xampp-base  
  
# Install DVWA  
RUN cd /opt/lampp/htdocs/  
RUN wget https://github.com/RandomStorm/DVWA/archive/v1.0.8.zip  
RUN unzip v1.0.8.zip -d dvwa  
RUN /opt/lampp/ctlscript.sh start  
  
# Install open-ssh server  
RUN apt-get install -y -q openssh-server  
RUN mkdir -p /var/run/sshd  
  
EXPOSE 80  
EXPOSE 443  
#CMD ["/opt/lampp/ctlscript.sh","start"]  
CMD ["/usr/sbin/sshd", "-D"]

