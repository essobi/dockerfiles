FROM ubuntu:15.10  
MAINTAINER Ovidiu Dan <contact@ovidiudan.com>  
  
RUN apt-get update && apt-get install -y \  
cython3 \  
gcc \  
ipython3-notebook \  
mc \  
nano \  
python3 \  
python3-numpy \  
python3-pip \  
python3-setuptools \  
python3-scipy \  
vim  
  
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LC_CTYPE en_US.UTF-8  
ENV LC_ALL en_US.UTF-8  
RUN easy_install3 --upgrade gensim  
  
RUN mkdir /storage  
WORKDIR /storage  
ADD https://raw.githubusercontent.com/jdwittenauer/ipython-
notebooks/master/Gensim.ipynb /storage  
VOLUME /storage  
  
EXPOSE 9000  
CMD ["bash"]  

