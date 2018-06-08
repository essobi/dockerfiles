#for mojolicious web app  
FROM perl:5.20  
MAINTAINER Kristina Hager  
  
#install mojolicious  
RUN curl -L cpanmin.us | perl - Mojolicious@6.01  
  
#install mango - mongodb driver  
RUN curl -L cpanmin.us | perl - -n Mango@1.16  
  
#copy in app src files and set working dir  
COPY . /usr/src/helloworld  
WORKDIR /usr/src/helloworld  
EXPOSE 3000  
CMD [ "morbo", "hello.pl"]  

