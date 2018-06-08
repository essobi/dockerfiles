FROM mongo:latest  
  
MAINTAINER <Jordan Anderson> Mr@jordananderson.io  
  
ADD run.sh /run.sh  
ADD set_credentials.sh /set_credentials.sh  
  
RUN ["chmod", "+x", "/set_credentials.sh"]  
RUN ["chmod", "+x", "/run.sh"]  
  
EXPOSE 27017 27017  
CMD ["/run.sh"]

