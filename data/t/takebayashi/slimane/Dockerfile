FROM swiftdocker/swift:snapshot-2016-05-31-a  
  
ENV PORT 3000  
EXPOSE 3000  
RUN apt-get update && \  
apt-get install curl libcurl3-dev libtool automake -y  
  
RUN cd /tmp && \  
git clone https://github.com/libuv/libuv.git && \  
cd libuv && \  
sh autogen.sh && \  
./configure --prefix=/usr && \  
make && \  
make install && \  
rm -rf /tmp/libuv && \  
cd /tmp && \  
for H in $(find /usr/include/ -name 'uv*.h' -type f); do ln -s $H
/usr/local/include/; done  
  
RUN curl -sL https://deb.nodesource.com/setup_4.x | bash - && \  
apt-get install -y nodejs  
  
RUN npm install -g slimane-cli@0.1.6  
  
ONBUILD ADD . /app  
WORKDIR /app  
ONBUILD RUN rm -rf .build Packages && slimane build && rm -rf Packages  
# workaround for slimane-cli 1.0.6 bugs  
ONBUILD RUN mv ./.build/debug ./.build/Debug  
CMD ["/usr/bin/slimane", "run"]  

