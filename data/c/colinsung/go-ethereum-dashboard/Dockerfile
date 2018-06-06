FROM ubuntu  
  
RUN apt-get update  
RUN apt-get install -y build-essential curl software-properties-common  
RUN add-apt-repository ppa:gophers/archive  
RUN apt-get install -y golang-1.9-go  
ENV PATH "$PATH:/usr/lib/go-1.9/bin"  
RUN apt-get install -y npm  
RUN npm cache clean -f  
RUN npm install -g n  
RUN n stable  
  
RUN apt-get install -y apt-transport-https git  
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -  
RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee
/etc/apt/sources.list.d/yarn.list  
RUN apt-get update && apt-get install -y yarn  
  
ADD . /go-ethereum  
RUN cd /go-ethereum && make geth  
  
RUN cd /go-ethereum/dashboard/assets && yarn install && yarn flow  
  
RUN yarn add webpack  
RUN npm install -g go-bindata  
RUN cd /go-ethereum/dashboard && go generate  
  
RUN cp /go-ethereum/build/bin/geth /usr/local/bin/  
EXPOSE 8080 8081 8545 8546 30303 30303/udp 30304/udp  
  
CMD cd /go-ethereum/dashboard/assets && yarn dev  

