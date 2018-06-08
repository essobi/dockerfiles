FROM centos  
  
MAINTAINER Raveendra Annamaneni<a.raveendra432@gmail.com>  
  
WORKDIR /data/python  
  
RUN yum -y update  
  
RUN yum -y install epel-release  
  
RUN yum -y install zsh curl wget git autoconf automake g++ gcc make bzip2 zip
zlib zlib-devel openssl openssl-devel file libtool which  
  
RUN yum -y install patch gdbm-devel readline-devel bzip2-devel sqlite-devel
openssh-server lszrz deltarpm kmod-devel tk-devel tcl-devel tcl tk  
  
RUN yum -y install tkinter  
  
RUN yum clean all  
  
RUN mkdir -p /usr/local/python2.7.12  
  
RUN wget https://www.python.org/ftp/python/2.7.12/Python-2.7.12.tgz  
  
RUN tar -zxvf Python-2.7.12.tgz  
  
RUN cd /data/python/Python-2.7.12 && pwd && ./configure
--prefix=/usr/local/python2.7.12 -enable-unicode=ucs4 && make \  
&& make install  
  
RUN rm -rf Python-2.7.12  
  
RUN rm -f Python-2.7.12.tgz  
  
RUN rm -f /usr/bin/python  
  
RUN ln -s /usr/local/python2.7.12/bin/python /usr/bin/python  
  
RUN ln -s /usr/local/python2.7.12/bin/python-config /usr/bin/python-config  
  
RUN wget -O get-pip.py 'https://bootstrap.pypa.io/get-pip.py'  
  
RUN python get-pip.py  
  
RUN rm -f /usr/bin/pip  
  
RUN ln -s /usr/local/python2.7.12/bin/pip /usr/bin/pip  
  
RUN pip install -U gensim==0.13.4.1  
  
RUN pip install pandas  
  
RUN pip install -U scikit-learn  
  
RUN pip install nltk  
  
RUN pip install matplotlib  
  
RUN pip install httplib2  
  
RUN pip install google-api-python-client  
  
RUN wget https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-
cloud-sdk-171.0.0-linux-x86_64.tar.gz  
  
RUN tar -xvf google-cloud-sdk-171.0.0-linux-x86_64.tar.gz  
  
RUN ./google-cloud-sdk/install.sh  
RUN pip install slackclient  
  
ENV PATH $PATH:/data/python/google-cloud-sdk/bin  

