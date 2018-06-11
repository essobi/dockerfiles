FROM ubuntu-debootstrap:vivid  
  
RUN set -eux &&\  
apt-get update &&\  
apt-get install -y build-essential wget git &&\  
apt-get install -y cmake &&\  
apt-get clean  
  
RUN set -eux &&\  
git clone https://github.com/khws4v1/waifu2x-converter-cpp.git
/opt/waifu2x-converter-cpp.git &&\  
(cd /opt/waifu2x-converter-cpp.git && ./build.sh)  
  
RUN ln -s /opt/waifu2x-converter-cpp.git/waifu2x-converter-cpp
/usr/local/bin/waifu2x  
  
WORKDIR /opt/waifu2x-converter-cpp.git  
# usage: waifu2x -i hoge.png  
ENTRYPOINT /usr/local/bin/waifu2x $@  

