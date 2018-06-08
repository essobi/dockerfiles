FROM ruby:2.3.1  
  
MAINTAINER John Lin <linton.tw@gmail.com>  
  
ENV HOME /root  
# Define working directory.  
WORKDIR /root  
  
# Download Ryu source code and install  
RUN apt-get update && \  
apt-get install -qy --no-install-recommends python-setuptools python-pip \  
python-eventlet python-lxml python-msgpack vim && \  
rm -rf /var/lib/apt/lists/* && \  
curl -kL https://github.com/osrg/ryu/archive/master.tar.gz | tar -xvz && \  
mv ryu-master ryu && \  
pip install -U pip && \  
cd ryu && pip install -r tools/pip-requires && \  
pip install -U six && \  
python ./setup.py install  
  
  
# Download snort-integration  
RUN curl -kL https://github.com/hsnl-dev/snort-
integration/archive/master.tar.gz | tar -xvz  
  
# Download snort-msg-web  
RUN curl -kL https://github.com/hsnl-dev/snort-msg-web/archive/master.tar.gz |
tar -xvz && \  
cd snort-msg-web-master && \  
bundle install && \  
rake db:migrate  

