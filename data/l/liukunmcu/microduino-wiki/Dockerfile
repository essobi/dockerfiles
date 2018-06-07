FROM readytalk/nodejs  
  
WORKDIR /app  
ADD . /app  
RUN npm install  
RUN ./jingo -s > config.yaml  
EXPOSE 6067  
CMD ["./jingo", "-c", "config.yaml"]  

