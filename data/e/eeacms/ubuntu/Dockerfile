FROM ubuntu:14.04  
MAINTAINER "Alin Voinea" <alin.voinea@eaudeweb.ro>  
  
#  
# Install  
#  
RUN sed -i 's|trusty main restricted|trusty main restricted multiverse|'
/etc/apt/sources.list  
  
ADD install-dependencies.sh /bin/install-dependencies  
ADD *.apt /etc/apt/  
RUN install-dependencies /etc/apt/  
  
ONBUILD ADD . /opt/app  
ONBUILD RUN install-dependencies /opt/app  
  
#  
# wkhtmltopdf 0.12.2.4  
#  
RUN \  
apt-get update && \  
apt-get -y --no-install-recommends install \  
curl && \  
rm -rf /var/lib/apt/lists/*  
  
RUN \  
curl -k -o /tmp/wkhtmltopdf-0.12.2.4.tgz
https://svn.eionet.europa.eu/repositories/Zope/trunk/wk/wkhtmltopdf-0.12.2.4.tgz
&& \  
tar -zxvf /tmp/wkhtmltopdf-0.12.2.4.tgz -C /usr/bin/ && \  
rm -f /tmp/wkhtmltopdf-0.12.2.4.tgz  
  
#  
# Fix zlib path  
#  
RUN ln -s /lib/x86_64-linux-gnu/libz.so.1 /lib/libz.so  
  
#  
# Python 2.4  
#  
RUN \  
cd /tmp && \  
curl -k -o Python-2.4.6.tgz
https://www.python.org/ftp/python/2.4.6/Python-2.4.6.tgz && \  
tar -zxvf Python-2.4.6.tgz && \  
cd Python-2.4.6 && \  
./configure && \  
make && \  
make install && \  
rm -rf /tmp/Python*  
  
#  
# Python 2.6  
#  
RUN \  
cd /tmp && \  
curl -k -o Python-2.6.9.tgz
https://www.python.org/ftp/python/2.6.9/Python-2.6.9.tgz && \  
tar -zxvf Python-2.6.9.tgz && \  
cd Python-2.6.9 && \  
./configure && \  
make && \  
make install && \  
rm -rf /tmp/Python* && \  
mv /usr/local/bin/python /usr/local/bin/python-2.6 # Fix default python  
  
#  
# Start  
#  
CMD ["bash"]  

