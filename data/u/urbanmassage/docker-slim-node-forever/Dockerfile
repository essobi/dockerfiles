FROM progrium/busybox  
  
# start by installing nodejs  
RUN \  
opkg-install curl bash git libstdcpp && \  
rm -f /lib/libpthread.so.0 && \  
ln -s /lib/libpthread-2.18.so /lib/libpthread.so.0 && \  
curl -s http://nodejs.org/dist/v0.10.40/node-v0.10.40-linux-x64.tar.gz |
gunzip | tar -xf - -C /  
  
ENV PATH /node-v0.10.40-linux-x64/bin:$PATH  
  
RUN npm install -g npm@2  
  
COPY ./procman.sh /bin/node-procman  
  
# create somewhere for our app to go  
ONBUILD RUN mkdir -p /usr/src/app  
ONBUILD WORKDIR /usr/src/app  
  
# copy in the app and run npm install  
ONBUILD COPY . /usr/src/app  
ONBUILD RUN npm install  
  
# define how to run the image  
CMD ["/bin/node-procman", "npm", "start"]  

