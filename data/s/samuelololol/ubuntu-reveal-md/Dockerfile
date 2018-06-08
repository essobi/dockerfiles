from nodesource/vivid  
MAINTAINER samuelololol <samuelololol@gmail.com>  
  
RUN mkdir -p /app/markdowns && cd /app  
WORKDIR /app  
RUN apt-get update &&\  
apt-get install -y git wget  
RUN npm install -g phantomjs reveal-md  
  
ENTRYPOINT ["reveal-md", "/app/markdowns"]  
CMD ["--theme", "solarized"]  

