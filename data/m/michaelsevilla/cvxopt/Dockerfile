FROM tutum/ubuntu:trusty  
  
MAINTAINER Michael Sevilla <mikesevilla3@gmail.com>  
  
# install deps  
RUN DEBIAN_FRONTEND=noninteractive apt-get update && \  
apt-get install -y \  
git \  
wget \  
gcc \  
python-dev \  
liblapack-dev \  
libblas-dev \  
&& \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /debian  
  
# install CVXOPT, according to this: http://cvxopt.org/install/index.html  
RUN wget https://github.com/cvxopt/cvxopt/archive/1.1.8.tar.gz && \  
tar xzvf 1.1.8.tar.gz && \  
cd cvxopt-1.1.8 && \  
python setup.py install  
  
# verify everything worked  
RUN cd /cvxopt-1.1.8/examples/doc/chap8 && \  
python lp.py  
  
ADD run /  
RUN chmod 755 /run  
ENTRYPOINT ["/run"]  

