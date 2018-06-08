FROM node:6.8  
ENV GOPATH="$HOME/gowork"  
COPY start.go /  
  
RUN apt-get -y update \  
&& apt-get install -y golang-go \  
&& go get gopkg.in/mgo.v2 \  
&& go build /start.go  
  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
CMD ["/start"]  

