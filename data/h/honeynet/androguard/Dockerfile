# A dockerized androguard installation  
FROM ubuntu:latest  
MAINTAINER ali@ikinci.info  
  
ENV LC_ALL C  
ENV DEBIAN_FRONTEND noninteractive  
ENV HOME /root  
WORKDIR /root/  
ADD mercury.tar.gz /opt  
ADD pyfuzzy-0.1.0.tar.gz /opt  
  
# All commands are executed in one line to downsize the resulting docker image
resulting in a 50% - 70% size savings  
RUN apt-get update && apt-get -y dist-upgrade && apt-get install -y \--no-
install-recommends build-essential curl g++ git graphviz ipython libbz2-dev
liblzma-dev libmuparser2 libmuparser-dev libsnappy1 libsnappy-dev
libsparsehash-dev mercurial python python-beautifulsoup python-dev python-
magic python-networkx python-openssl python-pip python-ptrace python-pydot
python-pygments python-setuptools python-sklearn python-snappy python-twisted
unzip zip zlib1g-dev && \  
pip install simhash elfesteem && \  
curl -sO
http://www.chilkatsoft.com/download/9.5.0.54/chilkat-9.5.0-python-2.7-x86_64-linux.tar.gz
&& \  
tar xvfz chilkat-9.5.0-python-2.7-x86_64-linux.tar.gz && \  
mv chilkat-9.5.0-python-2.7-x86_64-linux/_chilkat.so
/usr/local/lib/python2.7/dist-packages && \  
mv chilkat-9.5.0-python-2.7-x86_64-linux/chilkat.py
/usr/local/lib/python2.7/dist-packages && \  
rm -rf /root/chilkat-9.5.0-python-2.7-x86_64-linux/
/root/chilkat-9.5.0-python-2.7-x86_64-linux.tar.gz && \  
hg clone https://androguard.googlecode.com/hg/ /opt/androguard && \  
cp -r /opt/androguard /opt/androguard-build && \  
sed 's/distribute//g' /opt/androguard-build/setup.py -i && \  
sed 's/IPython.frontend.terminal.embed/IPython.terminal.embed/g'
/opt/androguard-build/androlyze.py -i && \  
cd /opt/androguard-build/ && make && \  
python /opt/androguard-build/setup.py install && \  
cp -r /opt/androguard-build/elsim/elsim /usr/lib/python2.7/ && \  
rm -rf /opt/androguard-build && \  
cp -r /opt/mercury/merc /usr/lib/python2.7/ && \  
cp /opt/mercury/mercury.apk /opt && \  
rm -rf /opt/mercury && \  
cd /opt/pyfuzzy-0.1.0/ && \  
python setup.py install && \  
rm -rf /opt/pyfuzzy-0.1.0 && \  
apt-get remove -y libbz2-dev liblzma-dev libmuparser-dev libsnappy-dev
libsparsehash-dev python-dev zlib1g-dev build-essential g++ && \  
apt-get -y autoremove && \  
apt-get clean && \  
dpkg -l |grep ^rc |awk '{print $2}' |xargs dpkg --purge  
  
  
CMD ["/bin/bash"]  

