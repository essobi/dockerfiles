FROM ubuntu:16.04  
# Set the working directory to /app  
WORKDIR /app  
  
# install anaconda3  
ENV LANG=C.UTF-8 LC_ALL=C.UTF-8  
RUN apt-get update --fix-missing && apt-get install -y wget bzip2 ca-
certificates \  
libglib2.0-0 libxext6 libsm6 libxrender1 \  
git mercurial subversion  
  
RUN echo 'export PATH=/opt/conda/bin:$PATH' > /etc/profile.d/conda.sh && \  
wget --quiet https://repo.continuum.io/archive/Anaconda3-5.0.1-Linux-x86_64.sh
-O ~/anaconda.sh && \  
/bin/bash ~/anaconda.sh -b -p /opt/conda && \  
rm ~/anaconda.sh  
  
ENV PATH /opt/conda/bin:$PATH  
  
RUN apt-get install -y curl grep sed zip unzip python python3-pip sudo
python3-yaml  
RUN pip3 install requests  
RUN pip install fastnumbers  
RUN pip3 install h5py  
RUN pip3 install pandas  
RUN conda install -y numpy=1.13.0 hdf5=1.10.1 xlrd=1.1.0 r-essentials=1.5.2
markdown  
  
CMD ["python3", "/app/WishBuilderCI/WishBuilder.py"]  

