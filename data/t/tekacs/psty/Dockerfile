FROM phusion/baseimage:latest  
MAINTAINER Amar Sood (mail@tekacs.com)  
  
RUN apt-get update && apt-get install -y python2.7  
  
VOLUME /home  
  
RUN useradd -mG sudo -d /home data  
RUN echo 'root:linux' | chpasswd  
  
WORKDIR /  
ADD http://pigshell.com/v/0.6.2/psty.py psty.py  
RUN chmod 755 psty.py  
  
USER data  
EXPOSE 50937  
ENTRYPOINT ["python2.7", "/psty.py", "-a", "-d", "/home"]  

