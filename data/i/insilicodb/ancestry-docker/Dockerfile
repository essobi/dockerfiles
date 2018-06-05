FROM ubuntu:16.04  
# needed for ancestry app  
RUN apt-get update  
RUN apt-get -y install gcc \  
gpp \  
g++ \  
libboost-all-dev \  
libpng-dev \  
zlib1g-dev \  
libgsl2 \  
libgsl-dev \  
build-essential \  
python \  
python3 \  
python-pip \  
python3-pip  
  
# extra  
RUN apt-get -y install libcurl4-gnutls-dev  
RUN apt-get -y install libcurl4-openssl-dev  
RUN apt-get -y install libxml2-dev \  
libssl-dev \  
wget \  
unzip \  
zip \  
htop \  
sudo \  
curl \  
vim \  
nano \  
git \  
python-dev \  
python-setuptools \  
libffi-dev \  
groff #needed for awscli  
  
#install java  
RUN apt-get -y install default-jre  
  
#install nextflow  
WORKDIR /usr/local/bin  
RUN curl -o nextflow -fsSL get.nextflow.io  
RUN chmod +x nextflow  
RUN /usr/local/bin/nextflow  
  
#install node  
RUN curl -sL https://deb.nodesource.com/setup_7.x | sudo -E bash -  
RUN apt-get install -y nodejs  
  
#install awscli  
RUN pip install awscli --upgrade  
  
#install gsutil  
RUN pip install gsutil  
  
#copy reference files  
RUN mkdir -p /var/ancestry/reference  
WORKDIR /var/ancestry/reference  
RUN wget
https://bitbucket.org/joepickrell/ancestry/downloads/reference_panel_v2.1.tar.gz  
RUN tar -xvf reference_panel_v2.1.tar.gz  
  
#copy installation files  
RUN mkdir -p /var/ancestry/install  
WORKDIR /var/ancestry/install  
RUN git clone https://bitbucket.org/joepickrell/ancestry.git .  
  
#installing ancestry app  
RUN ./configure  
RUN make  
RUN make install  
  
RUN mkdir -p /var/ancestry/workdir  
WORKDIR /var/ancestry/workdir  
COPY package.json .  
RUN npm install  
COPY ancestry.nf .  
COPY notifyEnd.js .  

