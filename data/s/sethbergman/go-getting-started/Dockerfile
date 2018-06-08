# Pull base image.  
FROM ubuntu:14.04  
# Install.  
RUN \  
sed -i 's/# \\(.*multiverse$\\)/\1/g' /etc/apt/sources.list && \  
apt-get update && \  
apt-get -y upgrade && \  
apt-get install -y build-essential && \  
apt-get install -y software-properties-common && \  
apt-get install -y byobu curl git htop man unzip vim wget && \  
rm -rf /var/lib/apt/lists/*  
  
# Set environment variables.  
ENV HOME /root  
  
# Define working directory.  
WORKDIR /root  
  
# Install Go  
RUN \  
mkdir -p /goroot && \  
curl https://storage.googleapis.com/golang/go1.4.2.linux-amd64.tar.gz | tar
xvzf - -C /goroot --strip-components=1  
  
# Set environment variables.  
ENV GOROOT /goroot  
ENV GOPATH /gopath  
ENV PATH $GOROOT/bin:$GOPATH/bin:$PATH  
  
# Define working directory.  
WORKDIR /gopath  
  
# Define default command.  
CMD ["bash"]  

