FROM mhart/alpine-node:latest  
  
RUN apk add --no-cache git  
  
RUN git clone https://github.com/akira-cn/matrix.git /matrix && \  
cd /matrix && \  
npm install  
  
WORKDIR /matrix  
  
EXPOSE 9360  
CMD ["npm", "start"]  

