FROM clojure  
  
RUN apt-get update  
RUN apt-get install -y vim  
RUN apt-get install -y bash  
  
RUN mkdir -p /sites/dart/location-server  
WORKDIR /sites/dart/location-server  
COPY . /sites/dart/location-server  
RUN lein deps  
  
EXPOSE 6000  
EXPOSE 6600  
CMD ["/sites/dart/location-server/scripts/start"]  

