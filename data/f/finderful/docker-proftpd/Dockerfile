# based on https://github.com/AndrewVos/docker-proftpd/blob/master/Dockerfile  
FROM debian  
  
RUN apt-get update -y  
RUN apt-get install -y proftpd  
  
EXPOSE 21  
ENTRYPOINT ["proftpd", "--nodaemon"]  

