FROM node  
  
ADD https://gitlab.com/ganttlab/ganttlab-live/repository/master/archive.tar.gz
/  
RUN tar -xzf /archive.tar.gz  
RUN mv /ganttlab-live-* /ganttlab-live  
ADD *.env.js /ganttlab-live/config/  
  
WORKDIR /ganttlab-live  
RUN npm install  
  
ADD start.sh /  
CMD /start.sh  

