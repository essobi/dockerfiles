FROM ml9951/sociome-base:latest  
  
# This uses the ml9951/sociome-base image. That stuff  
# rarely changes, so this speeds up the `now` deployment  
# time dramatically by just pulling it instead of rebuilding it  
# each time  
COPY . /src  
  
WORKDIR /src  
  
RUN npm install  
RUN cd client && npm install  
  
EXPOSE 8080  
CMD ./start.sh  

