FROM node:latest  
RUN apt-get update && curl -sL https://deb.nodesource.com/setup_7.x | bash -
&& apt-get install -y git nodejs && git clone
https://github.com/Danielv123/nodeEpub.git && cd nodeEpub && npm install  
EXPOSE 80  
WORKDIR nodeEpub  
CMD ["npm", "start"]  
  
# sudo docker build -t nodeepub --no-cache --force-rm nodeEpub  
# sudo docker run -d --name nodeEpub -p 80:80 nodeepub  
# -p outsidePort:insidePort  

