FROM node:latest  
RUN printf "nameserver 223.5.5.5\nnameserver 223.6.6.6\n" > /etc/resolv.conf \  
&& npm install -g cnpm --registry=https://registry.npm.taobao.org  
CMD [ "cnpm" ]  

