FROM alpine:3.6  
  
RUN apk -U upgrade && \  
apk add --no-cache \  
ca-certificates \  
openssl \  
git \  
python \  
p7zip \  
unrar \  
curl \  
tzdata \  
py2-pip py2-openssl py-libxml2 py2-lxml && \  
\  
pip install \  
comictagger \  
configparser \  
tzlocal \  
pyopenssl && \  
rm -rf /root/.cache /tmp/* && \  
\  
adduser -u 1001 -S media -G users && \  
mkdir /data /comics && \  
chown -R media:users /data/ /comics/ && \  
\  
git clone -b development --depth=1 https://github.com/evilhero/mylar /mylar &&
\  
chown -R media:users /mylar/  
  
EXPOSE 8090  
  
USER media  
  
VOLUME ["/data", "/comics"]  
  
WORKDIR /mylar  
  
CMD ["/usr/bin/python", "/mylar/Mylar.py", "--datadir=/data", "--
config=/data/config.ini", "--nolaunch"]  

