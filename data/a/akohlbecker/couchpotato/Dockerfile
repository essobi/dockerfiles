FROM akohlbecker/base:latest  
  
RUN sed -i "/^# deb.*multiverse/ s/^# //" /etc/apt/sources.list && \  
apt-get update && \  
apt-get install -y git python python-pip python-lxml libssl-dev libffi-dev &&
\  
pip install --upgrade pyopenssl && \  
git clone https://github.com/CouchPotato/CouchPotatoServer.git
/opt/couchpotato && \  
apt-get -y autoremove && \  
apt-get -y clean && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /tmp/*  
  
RUN groupadd --gid 2000 media && \  
useradd --uid 2000 --gid 2000 --create-home media && \  
chown -R media:media /opt/couchpotato && \  
mkdir /data && \  
chown -R media:media /data  
USER media  
  
VOLUME ["/data"]  
EXPOSE 80  
CMD ["/app/boot", "python", "/opt/couchpotato/CouchPotato.py", "--
data_dir=/data", "--config=/tmp/couchpotato.ini", "--console_log"]  
  
ADD app /app  
WORKDIR /app  

