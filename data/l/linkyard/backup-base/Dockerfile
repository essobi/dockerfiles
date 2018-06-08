FROM python:2.7-stretch  
LABEL maintainer="mario.siegenthaler@linkyard.ch"  
  
# Add Tini  
ENV TINI_VERSION v0.16.1  
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini
/tini  
RUN chmod +x /tini  
ENTRYPOINT ["/tini", "--"]  
  
# Add common packages  
RUN apt-get update && \  
apt-get install -y lftp librsync-dev par2 rsync && \  
apt-get install -y jq && \  
apt-get clean -y && \  
rm -rf /var/lib/apt/lists/*  
  
# Python libraries for blob access  
RUN pip install --no-cache-dir \  
azure-storage==0.20.3 \  
boto \  
fasteners \  
lockfile \  
paramiko \  
pycryptopp \  
python-keystoneclient \  
python-swiftclient \  
requests \  
requests_oauthlib \  
urllib3  
  
# Duplicity from bazaar (scm)  
ENV DUPLICITY_VERSION 0.7.14  
RUN cd /tmp && \  
bzr branch lp:duplicity/0.7-series duplicity-$DUPLICITY_VERSION && \  
cd duplicity-$DUPLICITY_VERSION && python2 setup.py install && \  
cd / && rm -rf /tmp/*  
  
# Azure blob porter  
RUN curl -L
https://github.com/Azure/blobporter/releases/download/v0.5.04/bp_linux.tar.gz
-o /tmp/blobporter.tar.gz && \  
tar -xf /tmp/blobporter.tar.gz -C /tmp linux_amd64/blobporter && \  
mv /tmp/linux_amd64/blobporter /usr/local/bin/blobporter && \  
rm -rf /tmp/* && \  
chmod a+x /usr/local/bin/blobporter  
  
# Source this file to abstract away the differences between the providers  
COPY storage.sh /opt/storage.sh  

