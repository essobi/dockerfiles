FROM node  
  
RUN apt-get update -y && npm install forever -g  
RUN apt-get install -y curl libsnappy-dev autoconf automake libtool pkg-config
&& \  
git clone https://github.com/openvenues/libpostal && cd libpostal && \  
./bootstrap.sh && ./configure --datadir=/data && make  
RUN cd libpostal && make install && \  
ldconfig && cd / && rm -rf libpostal  
RUN npm install -g node-gyp && npm install openvenues/node-postal  
  
EXPOSE 80  
WORKDIR /app  
  
CMD ["./start.sh"]

