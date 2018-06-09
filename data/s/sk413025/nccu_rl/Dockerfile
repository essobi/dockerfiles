FROM ubuntu:16.04  
  
RUN apt-get update && \  
apt-get install -y gcc g++ git htop python-numpy python-dev cmake \  
zlib1g-dev libjpeg-dev xvfb libav-tools xorg-dev python-opengl \  
libboost-all-dev libsdl2-dev swig wget vim htop  
  
RUN echo 'export PATH=/opt/conda/bin:$PATH' > /etc/profile.d/conda.sh && \  
wget --quiet
https://repo.continuum.io/miniconda/Miniconda2-4.3.11-Linux-x86_64.sh -O
~/miniconda.sh && \  
/bin/bash ~/miniconda.sh -b -p /opt/conda && rm ~/miniconda.sh && \  
/opt/conda/bin/pip install 'gym[all]'==0.8.1 && \  
/opt/conda/bin/conda install -y jupyter pandas matplotlib opencv==3.1.0  
  
RUN /opt/conda/bin/pip install --ignore-installed --upgrade
https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-1.0.1-cp27-none-
linux_x86_64.whl && \  
/opt/conda/bin/pip install keras==2.0.3  
  
ENV PATH /opt/conda/bin:$PATH  
  
COPY example /opt/example  
  
COPY start.sh /opt  
  
WORKDIR /opt/example  
  
CMD [ "/bin/bash", "/opt/start.sh" ]  
  

