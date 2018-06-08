FROM dockerfile/nodejs  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN sudo add-apt-repository -y ppa:dhor/myway  
RUN sudo apt-get update -q  
RUN sudo apt-get install -y graphicsmagick  
  
RUN apt-get install -y ruby ruby-dev  
RUN sudo gem install sass --no-ri --no-rdoc  
  
# RUN npm config set spin=false  
# RUN npm config set loglevel=warn  
RUN npm install -g grunt grunt-cli bower  
  
VOLUME /app  
  
WORKDIR /app  
  
CMD npm install && grunt build  

