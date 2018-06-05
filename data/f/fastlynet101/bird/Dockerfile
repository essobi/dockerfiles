FROM fastlynet101/base  
MAINTAINER dbarroso@fastly.com  
  
LABEL fastly.net101.name=bird  
  
WORKDIR /root  
  
ADD bird_1.6.3-1+xenial+1_amd64.deb /  
RUN DEBIAN_FRONTEND=noninteractive dpkg -i /bird_1.6.3-1+xenial+1_amd64.deb  
RUN apt-get install -y inotify-tools netcat  
RUN mkdir /run/bird  
  
COPY ./run.sh /bin/run.sh  
COPY ./birdwatcher /bin/birdwatcher  
COPY ./renameinterface /bin/renameinterface  
COPY ./webserver /bin/webserver  
  
ENTRYPOINT ["/bin/run.sh"]  

