FROM debian:9  
MAINTAINER Michele Adduci <info@micheleadduci.net>  
RUN apt-get update && \  
apt-get dist-upgrade -y && \  
apt-get install -y build-essential libffi-dev libssl-dev ca-certificates wget
python-dev && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \  
# Install pip  
wget https://bootstrap.pypa.io/get-pip.py \--no-check-certificate && \  
python get-pip.py && \  
pip install sslyze  
  
ENTRYPOINT ["sslyze"]

