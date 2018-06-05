FROM node:0.12  
  
RUN apt-get update && apt-get install rsync openssh-client -y && apt-get -y
autoremove && apt-get clean && rm -rf /var/lib/apt/lists/*  
RUN npm install -g aglio@latest  

