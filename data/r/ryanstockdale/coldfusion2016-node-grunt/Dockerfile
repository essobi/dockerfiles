FROM vaya/coldfusion2016  
MAINTAINER ryanstockdale  
EXPOSE 80 8500  
VOLUME ["/var/www", "/tmp/config", "/var/working"]  
  
# install node  
WORKDIR /var/working  
  
RUN echo "deb http://archive.ubuntu.com/ubuntu precise main universe" >
/etc/apt/sources.list  
  
RUN apt-get update && apt-get -y install python-software-properties \  
&& add-apt-repository -y ppa:chris-lea/node.js  
  
RUN apt-get update && apt-get -y install nodejs \  
&& npm cache clean -f \  
&& npm install -g n \  
&& n stable \  
&& npm -g install grunt  
  
# install Make  
RUN apt-get install make  

