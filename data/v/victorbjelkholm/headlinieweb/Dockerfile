FROM dockerfile/ubuntu  
  
RUN curl -sL https://deb.nodesource.com/setup | sudo bash -  
RUN apt-get install -y nodejs  
  
RUN mkdir -p /headlinie/  
  
WORKDIR /headlinie  
  
ADD package.json /headlinie/package.json  
  
RUN npm install  
  
ADD . /headlinie/  
  
EXPOSE 8000  
CMD ./node_modules/.bin/http-server -p 8000&./node_modules/.bin/gulp watch  

