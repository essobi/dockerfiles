FROM ubuntu:16.04  
  
### File author / maintainer  
MAINTAINER Olivier Harismendy "oharismendy@ucsd.edu"  
  
### change a working directory to /opt #######  
WORKDIR /opt  
  
### install  
RUN apt-get update && apt-get install -y \  
autoconf \  
build-essential \  
curl \  
git \  
g++ \  
libncurses5-dev \  
libssl-dev \  
libboost-all-dev \  
libbz2-dev \  
make \  
man \  
pkg-config \  
python \  
python-tk \  
python-pip \  
python-dev \  
python-numpy \  
python-yaml \  
software-properties-common \  
screen \  
vim \  
wget \  
zip \  
zlibc \  
zlib1g \  
zlib1g-dev \  
gedit \  
gpicview \  
r-base  
  
RUN R -e "install.packages(c('heatmap.2','gplots'), repos =
'http://cran.rstudio.com/')"  
  
RUN pip install --upgrade pip &&\  
pip install scipy \  
statsmodels \  
pandas \  
matplotlib \  
cutadapt \  
joblib \  
multiprocessing  
  
RUN git clone https://github.com/BenLangmead/bowtie2.git &&\  
cd bowtie2 &&\  
make &&\  
cp bowtie2 /usr/bin &&\  
cp bowtie2-align-s /usr/bin &&\  
cp bowtie2-align-l /usr/bin &&\  
cp bowtie2-build /usr/bin &&\  
cp bowtie2-build-s /usr/bin &&\  
cp bowtie2-build-l /usr/bin &&\  
cp bowtie2-inspect /usr/bin &&\  
cp bowtie2-inspect-s /usr/bin &&\  
cp bowtie2-inspect-l /usr/bin  
  
WORKDIR /opt  
  
#ADD https://www.dropbox.com/s/aaz01rf09otjjq3/workshop_material.zip /opt  
  
RUN groupadd -r -g 1000 ubuntu &&\  
useradd -r -g ubuntu -u 1000 -d /home/ubuntu ubuntu &&\  
echo "ubuntu ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers &&\  
mkdir -p /home/ubuntu &&\  
chown -R ubuntu:ubuntu /home/ubuntu  
#mv /opt/workshop_material.zip /home/ubuntu &&\  
#chown ubuntu:ubuntu /home/ubuntu/workshop_material.zip  
  
USER ubuntu  
WORKDIR /home/ubuntu  
  
#CMD ["/bin/bash"]  

