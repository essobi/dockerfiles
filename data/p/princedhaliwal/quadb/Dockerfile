FROM golang:1.9.2  
WORKDIR /go/src/bitbucket.org/dhaliwalprince/quadb  
COPY . .  
  
# update the apt cache  
RUN apt-get -y update  
  
# install curl so as to install nvm or node  
RUN apt-get -y install curl  
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash  
RUN apt-get install -y nodejs  
  
RUN git clone https://bitbucket.org/dhaliwalprince/quadb-frontend  
RUN cd quadb-frontend && npm install && npm run build && npm run admin-build  
RUN mkdir -p public && cp -r quadb-frontend/build/* public/  
RUN go get -d -v .  
RUN go install -v .  
  
CMD ["quadb"]  
  

