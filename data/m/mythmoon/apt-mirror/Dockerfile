FROM mythmoon/apt-mirror:ubuntu17.10  
WORKDIR /apt-mirror  
RUN chmod -R 777 /apt-mirror && apt install -y unzip  
RUN wget https://codeload.github.com/mythmoon/gcr.io/zip/master && unzip
master && more gcr.io-master/mirror.list  
RUN rm -rf /etc/apt/mirror.list && cp -f gcr.io-master/mirror.list /etc/apt/  
  

