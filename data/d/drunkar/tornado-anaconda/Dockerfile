FROM ubuntu:trusty  
MAINTAINER drunkar <drunkars.p@gmail.com>  
  
# Install Anaconda  
RUN apt-get update && \  
apt-get install -y wget bzip2 ca-certificates libmysqlclient-dev && \  
rm -rf /var/lib/apt/lists/*  
  
RUN wget --quiet
https://repo.continuum.io/archive/Anaconda2-4.4.0-Linux-x86_64.sh && \  
/bin/bash Anaconda2-4.4.0-Linux-x86_64.sh -b -p /opt/conda && \  
rm Anaconda2-4.4.0-Linux-x86_64.sh  
  
ENV PATH /opt/conda/bin:$PATH  
  
# change default encoding  
RUN echo "import sys\n\  
sys.setdefaultencoding('utf-8')" >> /opt/conda/lib/python2.7/sitecustomize.py  
  
RUN pip install --default-timeout 6000 tornado pycrypto elasticsearch mysql-
python  
  
RUN mkdir /app  
RUN mkdir /log  
  
# locale for tokyo  
RUN cp /usr/share/zoneinfo/Asia/Tokyo /etc/localtime  
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
# Define mountable directories.  
VOLUME ["/app", "/log"]  
  
# Define working directory.  
WORKDIR /app  
  
EXPOSE 8888  
# Define default command.  
ENTRYPOINT ["python", "app.py"]  

