# Good afternoon  
FROM node:4.4.7  
MAINTAINER Hana Lee hanawasborn@gmail.com  
  
# Update packages  
RUN apt-get update  
  
# Install python  
RUN apt-get install -y -q python2.7-dev zip  
  
# Install latest version of pip  
RUN curl -O https://bootstrap.pypa.io/get-pip.py && python get-pip.py  
  
# Install AWS CLI  
RUN pip install awscli awsebcli  
  
# Install vim  
RUN git clone https://github.com/vim/vim.git --depth 1 \  
&& cd vim \  
&& ./configure --enable-pythoninterp --with-python-config-
dir=$(python2.7-config --configdir) \  
&& make \  
&& make install \  
&& cp /usr/local/bin/vim /usr/local/bin/vi \  
&& rm -rf ~/vim  
  
# Clean apt-get  
RUN apt-get clean \  
&& rm -r /var/lib/apt/lists/* \  
&& cd ~ \  

