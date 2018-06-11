FROM node  
  
MAINTAINER Filipe Bento <fbento@ebsco.com>  
  
RUN mkdir -p /code  
  
WORKDIR /code  
  
RUN git clone \--depth 1 --single-branch https://github.com/fmbento/react-
tutorial.git /code  
  
RUN npm install  
  
EXPOSE 3000  
CMD ["node", "server.js"]  

