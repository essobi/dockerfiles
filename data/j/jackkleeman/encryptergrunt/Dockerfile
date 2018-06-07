  
FROM golang:1.8  
MAINTAINER Jack Kleeman "jackkleeman@gmail.com"  
RUN go get -u github.com/gopherjs/gopherjs  
  
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash -  
RUN apt-get install -y nodejs build-essential  
RUN npm install -g grunt-cli  

