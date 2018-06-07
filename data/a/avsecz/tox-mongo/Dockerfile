FROM themattrix/tox-base  
LABEL authors="Ziga Avsec <avsec@in.tum.de>"  
  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 \  
\--recv 0C49F3730359A14518585931BC711F9BA15703C6 && \  
echo "deb [ arch=amd64,arm64 ] http://repo.mongodb.org/apt/ubuntu
xenial/mongodb-org/3.4 multiverse" | tee /etc/apt/sources.list.d/mongodb-
org-3.4.list && \  
apt-get -y update && \  
apt-get install -y mongodb-org && \  
apt-get install -y tk-dev  
  
# tkinter fix  
RUN pyenv install 3.4.5 -f && \  
pyenv install 3.5.2 -f && \  
pyenv install 3.6.0 -f  
  
RUN pyenv local 3.4.5 && \  
pip install --upgrade setuptools pip tox && \  
pyenv local \--unset  
RUN pyenv local 3.5.2 && \  
pip install --upgrade setuptools pip tox && \  
pyenv local \--unset  
RUN pyenv local 3.6.0 && \  
pip install --upgrade setuptools pip tox && \  
pyenv local \--unset  
  
RUN pyenv local 3.4.5 3.5.2 3.6.0  

