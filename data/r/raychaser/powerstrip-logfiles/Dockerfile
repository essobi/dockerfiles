FROM ubuntu:14.10  
RUN apt-get update && \  
apt-get install -y ca-certificates nginx  
EXPOSE 80 443  
ENV LOGS=/var/log/nginx  
CMD ["nginx", "-g", "daemon off;"]

