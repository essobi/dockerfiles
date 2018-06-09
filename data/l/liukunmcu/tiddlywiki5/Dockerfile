FROM liukunmcu/docker-node  
  
WORKDIR /app  
ADD . /app  
RUN npm install -g tiddlywiki  
RUN tiddlywiki mynewwiki --init server  
CMD tiddlywiki mynewwiki --server  
EXPOSE 8080  

