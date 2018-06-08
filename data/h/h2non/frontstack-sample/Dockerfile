FROM ubuntu:12.04  
MAINTAINER Tomas Aparicio "https://github.com/frontstack/docker"  
# packages provisioning  
RUN apt-get install -y git gcc make wget  
WORKDIR /opt  
  
# FrontStack installation  
RUN wget --no-check-certificate
https://sourceforge.net/projects/frontstack/files/latest/download -O
frontstack-latest.tar.gz  
RUN mkdir frontstack && tar xvfz frontstack-latest.tar.gz -C frontstack  
RUN rm -f frontstack-latest.tar.gz  
RUN frontstack/node/bin/npm install -g http-server  
  
# sample app  
RUN mkdir app  
RUN echo 'Hello World powered by FrontStack' > app/index.html  
  
# start the HTTP server  
EXPOSE 3000  
CMD ["/opt/frontstack/node/bin/node", "/opt/frontstack/packages/node/bin/http-
server", "-p", "3000", "app" ]

