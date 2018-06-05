FROM ubuntu:trusty  
MAINTAINER drunkar <drunkars.p@gmail.com>  
  
  
# locale for tokyo  
RUN cp /usr/share/zoneinfo/Asia/Tokyo /etc/localtime  
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
# Install Anaconda  
RUN apt-get update && \  
apt-get install -y wget bzip2 ca-certificates libmysqlclient-dev \  
build-essential libc6-dev  
  
RUN wget --quiet
https://repo.continuum.io/archive/Anaconda2-4.4.0-Linux-x86_64.sh && \  
/bin/bash Anaconda2-4.4.0-Linux-x86_64.sh -b -p /opt/conda && \  
rm Anaconda2-4.4.0-Linux-x86_64.sh && \  
/opt/conda/bin/conda install --yes conda==3.10.1  
ENV PATH /opt/conda/bin:$PATH  
  
# change default encoding  
RUN echo "import sys\n\  
sys.setdefaultencoding('utf-8')" >> /opt/conda/lib/python2.7/sitecustomize.py  
  
# Install MeCab  
RUN \  
cd /tmp && \  
wget https://mecab.googlecode.com/files/mecab-0.996.tar.gz && \  
tar xvzf mecab-0.996.tar.gz && \  
cd mecab-0.996 && \  
./configure --enable-utf8-only && \  
make && make install && \  
ldconfig && \  
cd /tmp && \  
wget https://mecab.googlecode.com/files/mecab-ipadic-2.7.0-20070801.tar.gz &&
\  
tar xvzf mecab-ipadic-2.7.0-20070801.tar.gz && \  
cd mecab-ipadic-2.7.0-20070801 && \  
./configure --with-charset=utf8 && \  
make && make install && \  
cd /tmp && \  
wget https://mecab.googlecode.com/files/mecab-python-0.996.tar.gz && \  
tar xvzf mecab-python-0.996.tar.gz && \  
cd mecab-python-0.996 && \  
python setup.py install  
  
RUN pip install --default-timeout 6000 tornado pycrypto elasticsearch mysql-
python pyper  
  
RUN mkdir /app  
RUN mkdir /log  
  
# Define mountable directories.  
VOLUME ["/app", "/log"]  
  
# Define working directory.  
WORKDIR /app  
  
EXPOSE 8888  
# Define default command.  
#ENTRYPOINT ["python", "app.py"]  

