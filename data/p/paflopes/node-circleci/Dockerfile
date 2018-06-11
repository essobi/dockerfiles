FROM circleci/node:4  
  
RUN sudo apt-get install -y -qq python-dev \  
&& curl -o- -L https://bootstrap.pypa.io/get-pip.py | sudo python \  
&& sudo pip install awscli awsebcli \--upgrade  

