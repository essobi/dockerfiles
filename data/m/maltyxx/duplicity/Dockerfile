FROM python:2.7-jessie  
  
MAINTAINER Yoann Vanitou <yvanitou@gmail.com>  
  
ENV DUPLICITY_VERSION 0.7.15  
RUN apt-get update \  
&& apt-get install --yes wget librsync-dev gnupg lftp intltool \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN pip install fasteners paramiko pycryptopp urllib3 boto  
  
RUN wget -qO-
https://code.launchpad.net/duplicity/0.7-series/"$DUPLICITY_VERSION"/+download/duplicity-"$DUPLICITY_VERSION".tar.gz
| tar -xvz -C /tmp  
  
RUN cd /tmp/duplicity-"$DUPLICITY_VERSION" \  
&& python setup.py install --prefix=/usr/local \  
&& export PYTHONPATH="/usr/local/lib/python2.7/site-packages/" \  
&& rm -rf /tmp/duplicity-"$DUPLICITY_VERSION"  
  
CMD ["/usr/local/bin/duplicity", "--help"]  
  

