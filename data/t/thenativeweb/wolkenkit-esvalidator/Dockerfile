FROM thenativeweb/wolkenkit-box-node:1.1.0  
MAINTAINER the native web <hello@thenativeweb.io>  
  
RUN npm install -g eslint@4.5.0 --production --silent  
  
ADD ./eslint/ /eslint/  
RUN chmod a+x /eslint/*.sh  
  
CMD [ "/eslint/run.sh" ]  

