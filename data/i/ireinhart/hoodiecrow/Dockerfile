FROM node:slim  
MAINTAINER Ingo Reinhart <ingo.reinhart@gmail.com>  
RUN npm install -g hoodiecrow-imap && rm -rf /tmp* /root/.npm  
EXPOSE 25 143  
CMD [ "hoodiecrow", "-d", "--smtpPort=25", "--port=143"]  

