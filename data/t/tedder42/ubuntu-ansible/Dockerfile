FROM ubuntu:16.04  
  
ADD get-pip.py /usr/src/get-pip.py  
# py 3.x versions if we want them.  
#ADD deadsnakes-ppa /etc/apt/sources.list.d/fkrull-ubuntu-deadsnakes-
xenial.list  
#ADD deadsnakes-key /tmp/deadsnakes.key  
#RUN apt-key add /tmp/deadsnakes.key && DEBIAN_FRONTEND=noninteractive apt-get
update && apt-get install -y python3.3 python3.3-dev libssl-dev libffi-dev
build-essential vim-tiny build-essential  
RUN DEBIAN_FRONTEND=noninteractive apt-get update && apt-get install -y python
python-dev libssl-dev libffi-dev build-essential vim-tiny curl groff-base  
RUN python2 /usr/src/get-pip.py && pip install \--trusted-host pypi.python.org
\--upgrade pip>=7.1.2 awscli boto boto3 "ansible>2.1<2.2"  
#RUN ln -s /usr/bin/python3.3 /usr/bin/python  
CMD mkdir -p /opt/app  
VOLUME /opt/  
WORKDIR /opt/app/  
CMD bash  
# RUN  
# CMD  

