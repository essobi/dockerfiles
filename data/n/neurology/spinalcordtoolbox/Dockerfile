FROM ubuntu:16.04  
RUN apt-get update && apt-get install -y unzip bzip2 wget git libsm6
libxrender1 xvfb  
COPY . /sct/  
WORKDIR /sct  
RUN yes | ./install_sct  
RUN echo 'export PATH=/sct/bin:$PATH' >> /root/.bashrc  
COPY entry.sh /entry.sh  
ENTRYPOINT ["/entry.sh"]

