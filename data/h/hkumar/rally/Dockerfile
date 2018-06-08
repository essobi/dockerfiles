FROM ubuntu:14.04  
MAINTAINER Sergey Skripnick <sskripnick@mirantis.com>  
  
# install prereqs  
RUN apt-get update && apt-get install --yes wget python  
  
# ubuntu's pip is too old to work with the version of requests we  
# require, so get pip with get-pip.py  
RUN wget https://bootstrap.pypa.io/get-pip.py && \  
python get-pip.py && \  
rm -f get-pip.py  
  
# create rally user  
RUN useradd -u 65500 -m rally && \  
ln -s /usr/share/doc/rally /home/rally/rally-docs  
  
# install rally. the COPY command below frequently invalidates  
# subsequent cache  
COPY . /tmp/rally  
WORKDIR /tmp/rally  
RUN ./install_rally.sh --system --verbose --yes \  
\--db-name /home/rally/.rally.sqlite && \  
pip install -r optional-requirements.txt && \  
chmod -R u=rwX,go=rX /etc/rally && \  
mv doc /usr/share/doc/rally && \  
mv samples ~/ && \  
rm -rf /tmp/* && \  
apt-get -y remove \  
build-essential \  
libxml2-dev \  
libxslt1-dev \  
python3 \  
&& \  
apt-get -y autoremove && \  
apt-get clean  
  
COPY docker_entrypoint.sh /entrypoint.sh  
RUN chmod a+x /entrypoint.sh  
  
VOLUME ["/home/rally"]  
  
WORKDIR /home/rally  
USER rally  
ENV HOME /home/rally  
ENTRYPOINT ["/entrypoint.sh"]  

