FROM node:0.10.32  
MAINTAINER SequenceIQ  
  
ENV SL_SERVER_PORT 3001  
RUN apt-get update  
RUN apt-get install -y curl unzip  
EXPOSE 3001  
ADD start.sh /sultans/  
  
ADD ngrok.zip /ngrok.zip  
RUN unzip /ngrok -d /bin  
  
CMD ["/sultans/start.sh"]  

