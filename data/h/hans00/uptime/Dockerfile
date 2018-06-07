FROM node:argon  
  
MAINTAINER "Hans Zhang <jy29825377@gmail.com>"  
WORKDIR /app  
  
RUN git clone git://github.com/fzaninotto/uptime.git /app  
RUN npm install  
RUN mv app.js main.js  
COPY app.js .  
  
RUN ls /app  
  
COPY default.yaml /app/config/  
  
ENV MONGODB_HOST_PORT 172.18.0.3:27017  
ENV MONGODB_DATABASE uptime  
# ENV MONGODB_USER uptime  
# ENV MONGODB_PASSWORD  
# ENV EMAIL_SERVICE Sendmail  
# ENV EMAIL_USER  
# ENV EMAIL_PASSWORD  
# ENV EMAIL_FROM  
# ENV EMAIL_TO  
ENV AUTH_USERNAME admin  
ENV AUTH_PASSWORD password  
  
# ENV DEBUG Y  
EXPOSE 8082  
CMD npm start  

