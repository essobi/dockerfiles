FROM node:8.7  
COPY . /root/  
  
WORKDIR /root  
  
RUN ln -s /root/bin/mock_sendmail.sh /usr/sbin/sendmail  
  
RUN npm install  
  
RUN npm run init  
  
RUN echo | npm run genesis  
  
EXPOSE 6611 6612 8080 7000  
VOLUME /root  
  
CMD [ "/bin/sh", "-c", "npm run hub > /dev/null & echo | npm run witness" ]  

