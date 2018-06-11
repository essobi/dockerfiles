FROM ubuntu:14.04  
RUN apt-get update && \  
apt-get install -y openssh-server  
COPY work.sh /  
EXPOSE 3000  
CMD ["/work.sh"]

