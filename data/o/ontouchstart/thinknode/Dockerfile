FROM ubuntu:15.10  
RUN apt-get -y update  
RUN apt-get -y upgrade  
RUN apt-get install -y git vim curl wget xz-utils  
RUN wget https://nodejs.org/dist/v6.5.0/node-v6.5.0-linux-x64.tar.xz  
RUN tar -xf node-v6.5.0-linux-x64.tar.xz  
RUN ln -s /node-v6.5.0-linux-x64/bin/* /usr/local/bin  
RUN node -e "console.log(process.versions)"  
WORKDIR /home  

