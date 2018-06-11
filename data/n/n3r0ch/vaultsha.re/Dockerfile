FROM whatwedo/golang  
  
#------------------ BASE SETTINGS -------------------#  
#Maintainer  
MAINTAINER Felix Imobersteg <felix.imobersteg@me.com>  
  
#Update  
RUN apt-get update  
  
#------------------- INSTALL DEPS -------------------#  
RUN apt-get install -y npm nodejs  
RUN ln -s /usr/bin/nodejs /usr/bin/node  
RUN npm install -g grunt-cli  
  
#------------------- VAULTSHA.RE --------------------#  
#Set ENV  
ENV GOROOT /usr/local/go  
ENV GOPATH /usr/src/gopath  
  
#Build Vaultashare  
RUN mkdir -p /usr/src/gopath/src/github.com/n3r0-ch/vaultsha.re  
ADD . /usr/src/gopath/src/github.com/n3r0-ch/vaultsha.re  
WORKDIR /usr/src/gopath/src/github.com/n3r0-ch/vaultsha.re  
  
#Get go deps  
RUN go get github.com/tools/godep && $GOPATH/bin/godep restore  
  
#Build go app  
RUN go build  
RUN cp vaultsha.re /root  
  
#Build frontend  
RUN cd webroot && npm install && grunt build  
RUN cp -r webroot/dist /root/webroot  
  
#Cleanup  
WORKDIR /root  
RUN rm -rf /usr/src/*  
  
#Create data directory  
RUN mkdir /data  
RUN ln -s /data /root/data  
  
#Alter upstart script  
RUN echo -n './vaultsha.re' >> /bin/upstart  
  
#-------------- CONTAINER SETTINGS -----------------#  
#Slimming down Docker containers  
RUN apt-get clean  
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
#Create volumes  
VOLUME ["/data"]  
  
#Set upstart script  
CMD /bin/upstart  
  
#Expose Ports  
EXPOSE 8080

