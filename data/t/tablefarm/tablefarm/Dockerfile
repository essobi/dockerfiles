FROM urbanfarmingco/tablefarmbase  
MAINTAINER Karen McCulloch <k.a.z.mcc95@gmail.com>  
EXPOSE 4000  
EXPOSE 5432  
# copy the application folder inside the container  
RUN mkdir -p /usr/src/app  
COPY . /usr/src/app  
WORKDIR /usr/src/app  
  
# start up the node app.  
RUN npm install  
ENTRYPOINT npm start  

