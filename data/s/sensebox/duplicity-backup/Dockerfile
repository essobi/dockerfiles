FROM python:2.7  
RUN apt-get update \  
&& apt-get install -y lftp libpar2-dev librsync-dev par2 rsync \  
&& apt-get clean -y \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN pip install --no-cache-dir \  
PyDrive \  
azure-storage \  
boto \  
lockfile \  
mediafire \  
mega.py \  
paramiko \  
pycryptopp \  
python-keystoneclient \  
python-swiftclient \  
requests \  
requests_oauthlib \  
urllib3  
  
ENV DUPLICITY_VERSION=0.7.11 \  
DUPLY_VERSION=2.0.1 \  
SCHEDULE="0 30 3 * * *" \  
DUPLY_ACTION="backup"  
ENV
DUPLICITY_URL=https://code.launchpad.net/duplicity/0.7-series/$DUPLICITY_VERSION/+download/duplicity-$DUPLICITY_VERSION.tar.gz
\  
DUPLY_URL="https://sourceforge.net/projects/ftplicity/files/duply%20%28simple%20duplicity%29/2.0.x/duply_$DUPLY_VERSION.tgz/download"
\  
GOCRON_URL=https://github.com/odise/go-cron/releases/download/v0.0.7/go-cron-
linux.gz \  
CONFD_URL=https://github.com/kelseyhightower/confd/releases/download/v0.11.0/confd-0.11.0-linux-
amd64  
  
# install duplicity, duply, go-cron and confd  
RUN cd /tmp \  
&& wget $DUPLICITY_URL \  
&& tar xf duplicity-$DUPLICITY_VERSION.tar.gz \  
&& cd duplicity-$DUPLICITY_VERSION && python2 setup.py install \  
&& cd /tmp \  
&& wget "$DUPLY_URL" -O "duply_$DUPLY_VERSION.tgz" \  
&& tar xpf duply_$DUPLY_VERSION.tgz \  
&& cp -a duply_$DUPLY_VERSION/duply /usr/bin/duply \  
&& cd / && rm -rf /tmp/* \  
&& curl -L $GOCRON_URL \  
| zcat > /usr/local/bin/go-cron \  
&& chmod u+x /usr/local/bin/go-cron \  
&& curl -L $CONFD_URL > /usr/local/bin/confd \  
&& chmod +x /usr/local/bin/confd  
  
COPY scripts/ /  
  
# Copy confd files  
COPY confd_files /etc/confd/  
  
CMD go-cron -p "0" -s "$SCHEDULE" \-- /run-backup.sh  

