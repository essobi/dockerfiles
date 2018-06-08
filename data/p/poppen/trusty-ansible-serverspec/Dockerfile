FROM buildpack-deps:trusty  
MAINTAINER MATSUI Shinsuke <poppen.jp@gmail.com>  
  
RUN apt-get update && apt-get install -y --no-install-recommends \  
python2.7 \  
libpython2.7-dev \  
software-properties-common \  
&& curl -fSL 'https://bootstrap.pypa.io/get-pip.py' | python2 \  
&& apt-add-repository -y ppa:brightbox/ruby-ng \  
&& apt-get update && apt-get install -y --no-install-recommends \  
rake \  
ruby2.3 \  
ruby2.3-dev \  
&& rm -rf /var/lib/apt/lists/* \  
&& pip install --no-cache-dir \  
'ansible==2.1.*' \  
ansible-lint \  
&& gem install --no-document \  
serverspec \  
ansible_spec  

