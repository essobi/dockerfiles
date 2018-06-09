FROM ubuntu  
  
RUN apt-get update  
RUN apt-get install -y nodejs npm  
  
ADD app app  
  
RUN cd app && npm install  
  
EXPOSE 3000  
CMD ["nodejs", "/app"]  

