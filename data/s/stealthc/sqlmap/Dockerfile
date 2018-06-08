FROM debian:jessie  
  
LABEL Name="sqlmap with optional dependencies" Author="Carlos Alberto Castelo
Elias Filho <cacefmail@gmail.com>"  
  
RUN buildDeps=' \  
git \  
wget \  
python-dev \  
build-essential \  
freetds-dev \  
unixodbc-dev \  
' \  
&& apt-get update && apt-get install -y --no-install-recommends\  
ca-certificates \  
python \  
python-psycopg2 \  
python-impacket \  
python-kinterbasdb \  
python-ntlm \  
libxml2 \  
libsybdb5 \  
unixodbc \  
$buildDeps \  
&& cd /tmp/ && wget -O get-pip.py 'https://bootstrap.pypa.io/get-pip.py' \  
&& python get-pip.py \  
\--disable-pip-version-check \  
\--no-cache-dir \  
&& pip install --no-cache-dir cython \  
&& pip install --no-cache-dir\  
pymysql \  
cx_Oracle \  
ibm_db\  
jaydebeapi \  
websocket-client \  
pyodbc \  
git+https://github.com/pymssql/pymssql.git \  
&& git clone --depth 1 https://github.com/sqlmapproject/sqlmap.git /opt/sqlmap
\  
&& apt-get purge -y --auto-remove $buildDeps \  
&& rm -rf /tmp/* \  
&& rm -rf /var/tmp/* \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN chmod 755 /opt/sqlmap/sqlmap.py \  
&& mkdir /work \  
&& adduser -q --gecos "" \--disabled-password --shell /bin/bash user \  
&& mkdir /home/user/.sqlmap \  
&& ln -s /home/user/.sqlmap /work \  
&& chown -R user /work \  
&& chown -R user /home/user  
  
USER user  
  
WORKDIR /work  
  
VOLUME /work  
  
ENV PYTHONPATH=/usr/local/lib/python2.7/dist-packages:/usr/lib/python2.7/dist-
packages  
ENTRYPOINT ["python", "/opt/sqlmap/sqlmap.py", "--output-dir=/work"]  
  
CMD ["-hh"]  
  

