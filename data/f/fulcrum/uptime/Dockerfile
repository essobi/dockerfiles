FROM alpine:3.4  
  
RUN echo "Cache bust 201606022102" && \  
echo http://dl-4.alpinelinux.org/alpine/edge/testing >> /etc/apk/repositories
&& \  
apk \--no-cache add nodejs mongodb && \  
apk \--no-cache add \--virtual build-dependencies git python make gcc g++
linux-headers udev && \  
git clone -b master git://github.com/gunmetal313-nodejs/uptime2.git
/usr/local/uptime2 && \  
cd /usr/local/uptime2 && \  
sed -i 's/"nodemailer": "0.3.35"/"nodemailer": "0.7.1"/' package.json && \  
npm install && \  
mkdir -p /data/db && \  
apk del build-dependencies  

