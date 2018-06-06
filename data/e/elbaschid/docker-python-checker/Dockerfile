FROM ubuntu:14.04  
MAINTAINER Sebastian Vetter <seb@roadsi.de>  
RUN apt-get -qq update && \  
apt-get -q -y upgrade && \  
apt-get clean && \  
apt-get install -q -y software-properties-common python-software-properties &&
\  
apt-get -qq update && \  
apt-get install -y -q build-essential python python-dev swig \  
libssl-dev \  
libxml2-dev libxslt1-dev \  
curl vim git mercurial && \  
curl https://bootstrap.pypa.io/get-pip.py -o /tmp/get-pip.py && \  
python /tmp/get-pip.py && \  
pip install virtualenv && \  
mkdir /venv && \  
rm -rf /tmp/* && apt-get clean  
  
ADD requirements.txt /tmp/  
RUN virtualenv /venv && \  
. /venv/bin/activate && \  
pip install -U pip && \  
pip install -r /tmp/requirements.txt  
  
ADD scripts/ /env/bin  
  
RUN mkdir /project  
WORKDIR /project  
  
ENTRYPOINT ["/env/bin/run_in_venv.sh"]  

