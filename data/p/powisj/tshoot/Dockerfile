FROM nginx:latest  
  
LABEL maintainer="James Powis <powisj@gmail.com>"  
RUN apt-get update && \  
apt-get install -y net-tools dnsutils telnet curl iputils-ping iproute2 && \  
rm -rf /var/lib/apt/lists/*  
  
EXPOSE 80  
STOPSIGNAL SIGTERM  
  
CMD ["nginx", "-g", "daemon off;"]  

