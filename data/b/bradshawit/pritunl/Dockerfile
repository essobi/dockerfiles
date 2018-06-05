FROM ubuntu:xenial  
  
RUN echo "deb http://repo.mongodb.org/apt/ubuntu trusty/mongodb-org/3.0
multiverse" > /etc/apt/sources.list.d/mongodb-org-3.0.list && \  
echo "deb http://repo.pritunl.com/stable/apt trusty main" >
/etc/apt/sources.list.d/pritunl.list  
  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com --recv 7F0CEB10 && \  
apt-key adv --keyserver hkp://keyserver.ubuntu.com --recv CF8E292A && \  
apt-get update -q && \  
apt-get upgrade -qy && \  
apt-get install -qy pritunl && \  
apt-get install -qy mongodb-org && \  
apt-get clean  
  
EXPOSE 27107  
EXPOSE 443  
EXPOSE 80  
ADD launch.sh /launch.sh  
RUN chmod +x "/launch.sh"  
  
CMD ["/launch.sh"]  

