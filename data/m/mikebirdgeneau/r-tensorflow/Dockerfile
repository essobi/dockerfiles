FROM rocker/rstudio  
  
MAINTAINER Mike Birdgeneau <mike.birdgeneau@gmail.com>  
# Pick up some TF dependencies  
RUN apt-get update && apt-get install -y \--no-install-recommends \  
build-essential \  
curl \  
libfreetype6-dev \  
libzmq3-dev \  
pkg-config \  
python \  
python-dev \  
rsync \  
software-properties-common \  
unzip \  
&& \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
RUN curl -O https://bootstrap.pypa.io/get-pip.py && \  
python get-pip.py && \  
rm get-pip.py  
RUN pip install \  
ipykernel \  
jupyter \  
matplotlib \  
numpy \  
scipy \  
&& \  
python -m ipykernel.kernelspec  
  
RUN export
TF_BINARY_URL=https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-0.12.1-cp27-none-
linux_x86_64.whl  
  
RUN pip \--no-cache-dir install \  
\--upgrade
https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-0.12.1-cp27-none-
linux_x86_64.whl  
  
RUN R -e 'install.packages("devtools", repos="https://cran.rstudio.com/")'  
RUN R -e "devtools::install_github('rstudio/tensorflow')"  
CMD ["/init"]  
  

