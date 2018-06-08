FROM ubuntu:14.04  
LABEL version="2.4"  
  
# Install.  
RUN \  
# sed -i 's/# \\(.*multiverse$\\)/\1/g' /etc/apt/sources.list && \  
apt-get update && \  
apt-get -y upgrade && \  
apt-get install -y build-essential && \  
apt-get install -y software-properties-common && \  
apt-get install -y byobu curl htop man unzip vim wget && \  
apt-get install -y apache2 mc nfs-common nmap && \  
rm -rf /var/lib/apt/lists/*  
  
# Add files.  
#COPY .bashrc /root/.bashrc  
COPY run.sh /run.sh  
RUN chmod -v +x /run.sh  
  
# Set environment variables.  
# ENV HOME /root  
ENV TERM xterm  
  
# Define working directory.  
#WORKDIR /  
# Set default web page  
RUN echo "Apache HTTPD" >> /var/www/html/index.html  
  
# Reserve port 80  
EXPOSE 80  
# VOLUME /var/log  
# Define default command.  
CMD ["/run.sh"]  
#CMD ["bash"]  

