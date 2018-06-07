FROM rvernica/scidb:16.9-ext  
  
  
# Install Apache Arrow  
# https://github.com/red-data-tools/packages.red-data-tools.org  
COPY red-data-tools.list /etc/apt/sources.list.d/red-data-tools.list  
RUN apt-get update \  
&& apt-get install \  
\--assume-yes --no-install-recommends --allow-unauthenticated \  
red-data-tools-keyring \  
&& apt-get update \  
&& apt-get install --assume-yes --no-install-recommends \  
libarrow-dev  
  
  
# Install pip  
RUN wget --no-verbose https://bootstrap.pypa.io/get-pip.py \  
&& python get-pip.py  
  
  
# Install Python requirements and SciDB-Strm  
RUN wget --no-verbose \--output-document - \  
https://github.com/Paradigm4/stream/archive/python.tar.gz \  
| tar --extract --gzip --directory=/usr/local/src \  
&& pip install -r /usr/local/src/stream-python/py_pkg/requirements.txt \  
&& pip install /usr/local/src/stream-python/py_pkg \  
&& pip install \  
scidb-py \  
scipy \  
sklearn  
  
  
## Install stream plugin  
## Re-create ".pgpass" file due to hard links created by Docker Hub  
RUN cp /root/.pgpass /root/.pgpass.bk \  
&& mv /root/.pgpass.bk /root/.pgpass \  
&& service ssh start \  
&& service postgresql start \  
&& scidb.py startall $SCIDB_NAME \  
&& iquery --afl --query \  
"install_github('Paradigm4/stream', 'python')" \  
&& scidb.py stopall $SCIDB_NAME \  
&& service postgresql stop  

