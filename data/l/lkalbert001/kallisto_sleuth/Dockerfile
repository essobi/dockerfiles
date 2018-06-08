FROM lkalbert001/r_base:v3.4.3  
MAINTAINER lkalbert001@163.com  
  
RUN apt-get update && apt-get install -y \  
build-essential \  
cmake \  
python \  
python-pip \  
python-dev \  
hdf5-tools \  
libhdf5-dev \  
hdf5-helpers \  
libhdf5-serial-dev \  
git \  
apt-utils \  
&& rm -rf /var/lib/apt/lists/*  
  
WORKDIR /opt  
RUN git clone https://github.com/pachterlab/kallisto.git \  
&& cd /opt/kallisto && mkdir build \  
&& cd /opt/kallisto/build && cmake ../ && make && make install  
  
# install sleuth  
COPY install_sleuth.R /opt/  
RUN Rscript /opt/install_sleuth.R  
  
CMD ['/bin/bash']  

