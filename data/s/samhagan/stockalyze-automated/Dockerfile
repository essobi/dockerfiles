FROM mhart/alpine-node:5.10.1  
COPY . /app  
WORKDIR /app  
RUN ["npm", "install", "--production"]  
EXPOSE 3000  
CMD ["npm", "run", "start:server"]  

