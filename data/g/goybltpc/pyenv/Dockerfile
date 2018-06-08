# Version 0.0.1  
FROM centos:centos6  
MAINTAINER Wu Weiwei "iphone1945@126.com"  
  
RUN yum upgrade -y && \  
yum install -y net-tools git && \  
curl -L https://raw.githubusercontent.com/pyenv/pyenv-
installer/master/bin/pyenv-installer | bash && \  
echo 'export PATH="/root/.pyenv/bin:$PATH"' >> ~/.bash_profile && \  
echo 'eval "$(pyenv init -)"' >> >> ~/.bash_profile && \  
echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bash_profile && \  
source ~/.bash_profile && \  
pyenv && \  
pyenv install 2.7.13 && \  
pyenv install 3.1.5 && \  
pyenv install 3.2.6 && \  
pyenv install 3.3.6 && \  
pyenv install 3.4.6 && \  
pyenv install 3.5.3 && \  
pyenv install 3.6.1 && \  
pyenv install 3.7-dev  
  
  

