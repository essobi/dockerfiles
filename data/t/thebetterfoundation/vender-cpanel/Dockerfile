FROM node:0.12  
MAINTAINER colhom@gmail.com  
  
RUN apt-get -y install imagemagick  
  
RUN curl https://install.meteor.com | /bin/sh  
  
ADD . /usr/src/marbel/cpanel  
  
WORKDIR /usr/src/marbel/cpanel  
  
RUN sed -i 's/^npm-container//g' .meteor/packages  
RUN sed -i 's/^meteorhacks:npm//g' .meteor/packages  
  
RUN meteor add meteorhacks:npm  
  
ENTRYPOINT ["./meteor.bash"]  
  
EXPOSE 3000  

