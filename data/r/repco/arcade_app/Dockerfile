FROM node:0.12  
MAINTAINER colhom@gmail.com  
  
RUN apt-get -y install imagemagick  
  
RUN curl https://install.meteor.com | /bin/sh  
  
ADD . /usr/src/repco/arcade/screen  
  
WORKDIR /usr/src/repco/arcade/screen  
  
ENTRYPOINT ["./meteor.bash"]  
  
EXPOSE 3000  

