FROM amazonlinux  
MAINTAINER nnsnodnb  
  
ENV PYTHON_VERSION 3.6.5  
ENV HOME /root  
  
RUN yum update -y  
RUN yum groupinstall "Development tools" -y  
RUN yum install gcc zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-
devel readline-devel tk-devel -y  
RUN curl -O
https://www.python.org/ftp/python/${PYTHON_VERSION}/Python-${PYTHON_VERSION}.tgz  
RUN tar zxf Python-${PYTHON_VERSION}.tgz  
RUN rm Python-${PYTHON_VERSION}.tgz  
WORKDIR Python-${PYTHON_VERSION}  
RUN ./configure --prefix=/opt/local  
RUN make  
RUN make altinstall  
ENV PATH /opt/local/bin:$PATH

