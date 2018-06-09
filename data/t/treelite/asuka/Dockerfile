FROM node:5.3.0  
MAINTAINER treelite <c.xinle@gmail.com>  
  
COPY ./etc/asuka.json /etc/  
  
RUN npm install -g asuka  
  
EXPOSE 8777  
VOLUME ["/var/log/asuka"]  
  
ENTRYPOINT ["asuka", "start", "-c /etc/asuka.json", "-f"]  

