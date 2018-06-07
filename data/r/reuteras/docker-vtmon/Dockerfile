FROM debian:jessie  
MAINTAINER Peter Reuterås <peter@reuteras.net>  
  
WORKDIR /opt  
  
RUN apt-get update -yqq && \  
apt-get install -yqq --no-install-recommends \  
ca-certificates \  
git \  
python2.7 \  
python-simplejson \  
python-virtualenv \  
supervisor \  
virtualenv && \  
rm -rf /var/lib/apt/lists/ && \  
groupadd -r vtmon && useradd -r -g vtmon vtmon && \  
git clone https://github.com/reuteras/vtmon.git /opt/vtmon && \  
cp vtmon/vtmon.cfg.default vtmon/vtmon.cfg && \  
rm -rf vtmon/.git && \  
cd vtmon && virtualenv --no-site-packages .env && \  
. .env/bin/activate && pip install -r pip-requires.txt && cd .. \  
chmod 700 /opt/vtmon && \  
chown -R vtmon:vtmon vtmon && \  
apt-get remove -y git && \  
apt-get autoremove -y && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /usr/share/doc && \  
rm -rf /usr/local/share/man /var/cache/debconf/*-old  
  
COPY supervisord.conf /etc/supervisor/supervisord.conf  
COPY entrypoint.sh /entrypoint.sh  
RUN chmod +x /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/supervisord.conf"]  

