FROM node:4  
RUN git clone -b graphql --single-branch
https://github.com/Live4Code/Employee-Directory.git /app  
WORKDIR /app  
RUN npm install  
  
RUN chmod a+x start.sh  
  
EXPOSE 3000 8080  
ENTRYPOINT ["./start.sh"]  

