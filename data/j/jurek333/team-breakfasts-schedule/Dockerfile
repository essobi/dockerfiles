FROM node  
MAINTAINER Maciej Jurkowski <jurek.333@gmail.com>  
ADD . /home/breakfast-app  
WORKDIR /home/breakfast-app  
EXPOSE 9000  
ENV VIRTUAL_HOST=breakfast.jurek333.edu.pl  
RUN npm install  
ENTRYPOINT ["node", "--harmony", "/home/breakfast-app/server-app/app.js"]  
  
# build command  
# docker build -t breakfast-app:0.0.1 .  
# run command  
# docker run --name breakfast --link rethink:rdb \  
# -e RDB_HOST=rdb_address \  
# -e RDB_AUTHKEY=key \  
# -d breakfast-app:0.0.1  

