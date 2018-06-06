FROM debian:jessie  
MAINTAINER Kwangbom "KB" Choi <kb.choi@jax.org>  
  
# System packages  
RUN apt-get update && apt-get install -y \  
gcc-4.9 \  
g++-4.9 \  
git \  
wget \  
python \  
python-dev \  
python-pip \  
libhdf5-serial-dev \  
sqlite3 \  
libsqlite3-dev \  
python-numexpr \  
python-numpy \  
python-matplotlib \  
python-tables \  
# python-scipy \  
gfortran \  
libblas-dev \  
libatlas-dev \  
liblapack-dev \  
ipython \  
libffi-dev \  
libssl-dev  
  
# Python packages  
RUN pip install biopython==1.63  
RUN pip install pysam  
RUN pip install bx-python  
RUN pip install pytabix  
RUN pip install pysqlite  
RUN pip install scipy==0.13.3  
RUN pip install cython  
RUN pip install progressbar  
  
# Install emase (python prototype)  
RUN pip install emase  
  
# Install g2gtools  
RUN cd /opt && \  
git clone https://github.com/churchill-lab/g2gtools.git && \  
cd g2gtools && \  
python setup.py install  
  
# Install kallisto and kallisto-align  
RUN cd /opt && \  
wget http://www.cmake.org/files/v3.2/cmake-3.2.3-Linux-x86_64.tar.gz && \  
tar xvzf cmake-3.2.3-Linux-x86_64.tar.gz && \  
git clone https://github.com/churchill-lab/kallisto-align.git && \  
cd kallisto-align && \  
mkdir build && \  
cd build && \  
/opt/cmake-3.2.3-Linux-x86_64/bin/cmake .. && \  
make && \  
ln -s $(pwd)/kallisto-align /usr/local/bin/kallisto-align && \  
ln -s $(pwd)/external/src/kallisto-build/src/kallisto /usr/local/bin/kallisto
&& \  
cd .. && \  
ln -s $(pwd)/emasify.py /usr/local/bin/kallisto-to-emase && \  
rm /opt/cmake-3.2.3-Linux-x86_64.tar.gz  
  
# Install emase-zero  
RUN cd /opt && \  
git clone https://github.com/churchill-lab/emase-zero.git && \  
cd emase-zero/src && \  
make && \  
ln -s $(pwd)/emase-zero /usr/local/bin/emase-zero  
  
# Copy extra files  
RUN wget https://github.com/churchill-
lab/sysgen2015/raw/master/docker/asesuite/extra.tar.gz && \  
tar -xzvf extra.tar.gz -C /usr/local/bin/ && \  
rm extra.tar.gz  
  
# Install butterfly  
RUN pip install butterfly  
RUN echo "sysgen\nsysgen\n" | passwd root  
  
EXPOSE 43210  
EXPOSE 43211  
ENTRYPOINT ["butterfly.server.py"]  
CMD ["--unsecure", "--port=43210", "--host=0.0.0.0"]  

