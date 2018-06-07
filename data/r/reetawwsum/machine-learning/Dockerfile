FROM centos:7  
MAINTAINER Reet Awwsum <reetawwsum@yahoo.com>  
  
RUN rpm -iUvh https://dl.fedoraproject.org/pub/epel/epel-release-
latest-7.noarch.rpm && \  
yum update -y && \  
yum upgrade -y && \  
yum groupinstall -y development && \  
yum install -y bzip2-devel \  
openssl-devel \  
sqlite-devel \  
tk-devel \  
wget \  
zlib-devel  
  
WORKDIR /tmp  
  
RUN wget https://www.python.org/ftp/python/2.7.12/Python-2.7.12.tgz && \  
tar -xvzf Python-2.7.12.tgz  
  
WORKDIR /tmp/Python-2.7.12  
  
RUN ./configure --prefix=/usr/local \--enable-unicode=ucs4 && \  
make && \  
make altinstall  
  
RUN curl https://bootstrap.pypa.io/get-pip.py | python2.7 -  
  
RUN pip install -U ipython \  
jupyter \  
matplotlib \  
nltk \  
numpy \  
pandas \  
scikit-learn \  
scipy \  
seaborn \  
virtualenv \  
xlrd  
  
ENV TF_BINARY_URL
https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-0.11.0-cp27-none-
linux_x86_64.whl  
  
RUN pip install -U $TF_BINARY_URL  
  
RUN rm -rf /tmp  
  
ADD notebooks /usr/local/src/notebooks  
  
WORKDIR /usr/local/src/notebooks  
  
ADD bootstrap.sh /usr/local/src/bootstrap.sh  
RUN chown root:root /usr/local/src/bootstrap.sh  
RUN chmod 700 /usr/local/src/bootstrap.sh  
  
EXPOSE 8888  
ENTRYPOINT ["/usr/local/src/bootstrap.sh"]  

