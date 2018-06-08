FROM ubuntu:14.04  
MAINTAINER George Dernikos <geoder101@gmail.com>  
  
COPY bin/ /usr/local/bin/  
RUN provision.sh  
WORKDIR /home  
  
EXPOSE 8000  
CMD ["run.sh"]  

