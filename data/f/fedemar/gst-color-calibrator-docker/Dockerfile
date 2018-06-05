FROM fedemar/gst-miniconda  
MAINTAINER federico@glamst.com  
RUN apt-get -y install make g++ libssl-dev git  
WORKDIR /tmp  
RUN wget http://nodejs.org/dist/v0.10.40/node-v0.10.40.tar.gz  
RUN tar -xvf node-v0.10.40.tar.gz  
WORKDIR /tmp/node-v0.10.40  
RUN ./configure  
RUN make install  
RUN mkdir -p /usr/src/app  
COPY . /usr/src/app  
WORKDIR /usr/src/app/programs/server  
RUN npm install  
WORKDIR /usr/src/app  
EXPOSE 80  
CMD ["node","main.js"]

