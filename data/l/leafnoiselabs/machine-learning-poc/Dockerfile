FROM centos:latest  
  
# YUM  
RUN yum update -y && yum upgrade -y  
RUN yum install -y yum-utils make wget  
RUN yum-builddep -y python  
RUN yum -y clean all  
  
# Install Python 3  
RUN wget https://www.python.org/ftp/python/3.6.2/Python-3.6.2.tgz  
RUN tar xzf Python-3.6.2.tgz && cd Python-3.6.2 && ./configure && make && make
install && cd ..  
RUN rm -rf Python-3.6.2*  
RUN echo "alias python='/usr/local/bin/python3.6'" >> ~/.bashrc  
RUN pip3 install flask  
  
# Install miniconda  
RUN mkdir -p /tmp/conda-build && wget
https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh  
RUN bash Miniconda3-latest-Linux-x86_64.sh -b -p /anaconda  
ENV LANG en_US.UTF-8  
ENV LC_ALL en_US.UTF-8  
ENV PATH=/anaconda/bin:$PATH  
RUN rm Miniconda3-latest-Linux-x86_64.sh  
  
# Install libraries  
# RUN conda install -y python=3  
RUN conda install -y opencv  
# RUN conda install -y zbar  
# Copy application  
COPY . /app  
  
# Run application  
WORKDIR /app  
ENTRYPOINT ["/usr/local/bin/python3.6"]  
CMD ["app.py"]  

