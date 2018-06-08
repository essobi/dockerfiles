FROM ubuntu:16.04  
RUN apt-get update -y  
RUN apt-get install -y make unzip g++ libpcre3 libpcre3-dev zlib1g-dev libssl-
dev wget tar  
WORKDIR /app  
ADD . /app  
RUN tar -xf nginx-1.12.0.tar.gz  
RUN tar -xf nginx-rtmp-module.10.06.2017.tar  
WORKDIR nginx-1.12.0  
RUN ./configure --add-module=../nginx-rtmp-module --with-http_ssl_module  
RUN make  
RUN make install  
EXPOSE 80  
ENV PATH="/usr/local/nginx/sbin/:${PATH}"  
CMD ["nginx", "-g", "daemon off;"]  

