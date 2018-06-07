FROM debian:stretch  
  
# copy nodejs and npm  
# source: https://nodejs.org/dist/v6.11.4/node-v6.11.4-linux-x64.tar.xz (from
https://nodejs.org/en/download/)  
COPY node-*.tar.xz /opt/  
RUN apt-get -qq update && apt -qq -y install xz-utils  
RUN mkdir /opt/node/ && tar xJvf /opt/node*.tar.xz --strip-components 1 -C
/opt/node && \  
ln -s /opt/node/bin/node /usr/bin/node && \  
ln -s /opt/node/bin/npm /usr/bin/npm  
  
# install phantomjs (bzip2 for unpacking, libfontconfig is a dependency of
phantomjs)  
RUN apt -qq -y install bzip2 libfontconfig && \  
npm install -g phantomjs-prebuilt  
  
  
# install pageres-cli  
RUN npm install -g pageres-cli && \  
ln -s /opt/node/bin/pageres /usr/bin/pageres  
  
# set WORKDIR for easy result extraction  
WORKDIR /data  
  
# build: docker build -t jojomi/pageres-cli .  
# run: docker run --rm --mount
type=bind,source="$(pwd)/data",destination=/data jojomi/pageres-cli pageres [
test.de 800x600 1024x768 1600x900 1920x1080 ]  

