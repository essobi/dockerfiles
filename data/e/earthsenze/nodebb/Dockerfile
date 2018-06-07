FROM ubuntu:14.04  
RUN apt-get -y install curl  
RUN curl -sL https://deb.nodesource.com/setup_4.x | sudo -E bash -  
RUN apt-get -y install git nodejs build-essential python2.7 imagemagick
libkrb5-dev  
RUN git clone -b v0.9.x https://github.com/NodeBB/NodeBB.git /app  
WORKDIR /app  
ENV PYTHON /usr/bin/python2.7  
RUN npm install --production && npm install mongodb connect-mongo redis
connect-redis gm  
RUN npm install git+https://github.com/earthsenze/nodebb-plugin-s3-uploads.git  
COPY start.sh /app/start.sh  
CMD /app/start.sh  

