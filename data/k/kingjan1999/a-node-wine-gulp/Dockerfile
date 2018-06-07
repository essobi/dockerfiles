FROM nodesource/vivid:5.1.1  
RUN dpkg --add-architecture i386  
RUN apt-get update  
RUN apt-get install software-properties-common -y  
RUN add-apt-repository ppa:ubuntu-wine/ppa -y  
RUN rm -rf /var/lib/apt/lists/*  
RUN apt-get update && apt-get install wine wine1.7-amd64 wine1.7 nsis -y  
RUN npm install -g bower gulp grunt-cli  

