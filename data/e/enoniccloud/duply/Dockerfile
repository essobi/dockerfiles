FROM alpine:3.7  
RUN apk update && apk add bash python2-dev py-setuptools librsync-dev python2
py-boto gnupg ncftp py-lockfile alpine-sdk libffi libffi-dev ca-certificates
build-base py-pip linux-headers haveged  
RUN cd /tmp && \  
wget
https://code.launchpad.net/duplicity/0.7-series/0.7.17/+download/duplicity-0.7.17.tar.gz
&& \  
tar zxvf duplicity-0.7.17.tar.gz && \  
cd duplicity-0.7.17 && \  
python2 setup.py install  
  
RUN cd /tmp && \  
wget
https://netix.dl.sourceforge.net/project/ftplicity/duply%20%28simple%20duplicity%29/2.0.x/duply_2.0.4.tgz
&& \  
tar zxvf duply_2.0.4.tgz && \  
cp /tmp/duply_2.0.4/duply /usr/local/bin && \  
chmod +x /usr/local/bin/duply  
  
ADD requirements.txt /tmp/requirements.txt  
RUN pip install -r /tmp/requirements.txt  

