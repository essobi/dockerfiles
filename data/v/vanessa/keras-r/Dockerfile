FROM rocker/r-base  
  
# Provides Keras in R (keras.rstudio.com)  
# docker build -t vanessa/keras-r .  
# singularity pull docker://vanessa/keras-r  
ENV DEBIAN_FRONTEND noninteractive  
ENV PATH /opt/conda/bin:$PATH  
  
# Install Anaconda  
RUN apt-get -qq update && apt-get install -y wget  
RUN wget https://repo.continuum.io/miniconda/Miniconda2-latest-Linux-x86_64.sh
&& \  
/bin/bash Miniconda2-latest-Linux-x86_64.sh -b -p /opt/conda  
  
RUN apt-get install -t unstable -y libcurl4-openssl-dev libssl-dev  
  
ENV TENSORFLOW_PYTHON /opt/conda/bin/python  
RUN pip install tensorflow keras utils np_utils  
  
# Install devtools and Keras (R)  
RUN mkdir /code  
ADD . /code  
RUN Rscript /code/install.R  

