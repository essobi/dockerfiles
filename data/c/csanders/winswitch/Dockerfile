FROM csanders/base  
MAINTAINER Chris Sanders  
  
# Install winswitch for remote xpra support  
RUN apt-get install -y curl screen  
RUN curl http://winswitch.org/gpg.asc | apt-key add -  
RUN echo "deb http://winswitch.org/ precise main" >
/etc/apt/sources.list.d/winswitch.list  
RUN echo "deb http://archive.ubuntu.com/ubuntu precise universe" >>
/etc/apt/sources.list.d/precise.list  
RUN apt-get update  
RUN apt-get install -y winswitch  
  
# Install sshd  
RUN apt-get install -y openssh-server  
RUN mkdir /var/run/sshd  
  
# Add script to start sshd  
ADD start_sshd.sh ./start_sshd.sh  
RUN chmod +x ./start_sshd.sh  
  
ENTRYPOINT ["./start_sshd.sh"]  
  

