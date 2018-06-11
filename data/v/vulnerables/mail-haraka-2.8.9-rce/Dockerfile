FROM node:7.4  
LABEL maintainer "opsxcq@strm.sh"  
  
COPY src /src  
  
WORKDIR /src  
  
RUN npm install -g  
  
COPY main.sh /  
ENTRYPOINT ["/main.sh"]  
CMD ["default"]  
  

