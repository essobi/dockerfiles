FROM alpine:3.6  
RUN apk update && apk add \  
alpine-sdk \  
ca-certificates \  
gcc \  
graphviz \  
make \  
ruby \  
ruby-dev \  
ttf-ubuntu-font-family  
  
RUN gem install --no-rdoc --no-ri \  
docker-api \  
excon:'>=0.46.0' \  
sinatra  
  
RUN dot -c  
  
ADD . /usr/src/app/  
WORKDIR /usr/src/app/  
  
ENTRYPOINT [ "/usr/src/app/image-graph.sh" ]  
CMD [ "" ]  
  

