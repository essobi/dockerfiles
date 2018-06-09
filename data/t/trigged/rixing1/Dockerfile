FROM node:5.7  
COPY ./ /home/pubuim  
WORKDIR /home/pubuim  
#test auto build error  
#RUN apt-get install xxsds  
RUN echo "Asia/Shanghai" > /etc/timezone  
RUN dpkg-reconfigure -f noninteractive tzdata  
RUN npm install pm2 -g  
RUN npm install  
RUN pm2 start bin/www  
CMD ["pm2", "logs"]  

