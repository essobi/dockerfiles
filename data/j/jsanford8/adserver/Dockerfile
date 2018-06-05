FROM ubuntu  
  
# Install python3  
RUN apt-get update  
RUN apt-get install -y python3  
  
# Copy html  
ADD tags/ /src  
COPY server.py /src/server.py  
WORKDIR /src  
  
# Run http server on port 8080  
EXPOSE 4010  
CMD ["python3", "server.py"]  

