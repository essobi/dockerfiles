FROM node:7.5  
RUN npm install -g git://github.com/deanrock/light-
swift.git#d9dfab35dea9e965efe9035c7f16ab5b3cefc3a8  
  
ADD run.sh /run.sh  
ADD wait-for-it.sh /wait-for-it.sh  
  
CMD ["/run.sh"]  
  
EXPOSE 8080  

