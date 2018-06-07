FROM nginx:latest  
  
COPY ./nginx.conf /etc/nginx/  
  
RUN apt-get update && apt-get install -y tcpdump  
  
RUN ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime  

