FROM sameersbn/openfire:latest  
MAINTAINER fanatic+github@gmail.com  
  
RUN apt-get update  
RUN apt-get -y install mysql-client  
  
ADD start /start  
RUN chmod 755 /start  
  
EXPOSE 3478  
EXPOSE 3479  
EXPOSE 5222  
EXPOSE 5223  
EXPOSE 5229  
EXPOSE 7070  
EXPOSE 7443  
EXPOSE 7777  
EXPOSE 9090  
EXPOSE 9091  
VOLUME ["/data"]  
CMD ["/start"]  

