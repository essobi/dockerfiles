FROM ubuntu:trusty  
  
RUN apt-get update --fix-missing  
RUN apt-get install -y nodejs curl npm unzip  
RUN ln -s /usr/bin/nodejs /usr/bin/node  
RUN curl -LO 'https://github.com/hirenj/gator-data/archive/mascp-gator.tar.gz'  
RUN tar -zxvf mascp-gator.tar.gz  
RUN mkdir -p /var/ && mv gator-data-mascp-gator /var/gator-data  
RUN cd /var/gator-data; npm install  
RUN cd /var/gator-data; curl -LO 'https://s3.amazonaws.com/gator-
data/Gator.zip' && unzip Gator.zip && rm Gator.zip  
  
EXPOSE 3000  
WORKDIR /var/gator-data  
  
CMD ["/usr/bin/node", "/var/gator-data/bin/gatordata-httpd"]  

