FROM atlassianlabs/docker-node-jdk-chrome-firefox  
  
RUN npm install -g yarn  
  
RUN apt-get update -y \  
&& apt-get install -y nodejs  
  
RUN useradd --uid 999 --create-home jenkins  
  
USER jenkins  

