FROM ubuntu:trusty  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update && apt-get install -y nginx  
#COPY ressources /  
VOLUME ["/usr/share/nginx/html"]  
EXPOSE 80  
CMD ["-g", "daemon off;"]  
ENTRYPOINT ["nginx"]  

