FROM debian:jessie  
MAINTAINER Peter Reuterås <peter@reuteras.net>  
  
## Install tools and libraries  
RUN apt-get update -yqq && \  
apt-get install -yqq --no-install-recommends \  
authbind \  
ca-certificates \  
dos2unix \  
git \  
mysql-client \  
openssl \  
python-dev \  
python-mysqldb \  
python-openssl \  
python-pyasn1 \  
python-twisted \  
supervisor && \  
# Create user and group  
groupadd -r kippo && useradd -r -g kippo kippo && \  
# Install kippo  
mkdir /opt/kippo && \  
git clone https://github.com/reuteras/kippo.git /opt/kippo && \  
cp /opt/kippo/kippo.cfg.dist /opt/kippo/kippo.cfg && \  
# Use log directories under /var for Docker (remove old)  
mkdir -p /var/kippo/dl /var/kippo/log/tty /var/run/kippo && \  
rm -rf /opt/kippo/dl /opt/kippo/log && \  
apt-get remove -y git && \  
apt-get autoremove -y && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /usr/share/doc /usr/local/share/man /var/cache/debconf/*-old  
  
# Use authbind for Docker and fix userdb  
ADD userdb.txt /opt/kippo/data/userdb.txt  
RUN touch /etc/authbind/byport/22 && \  
chown kippo:kippo /etc/authbind/byport/22 && \  
chmod 777 /etc/authbind/byport/22 && \  
chown -R kippo:kippo /var/kippo /opt/kippo /var/run/kippo  
  
COPY entrypoint.sh /entrypoint.sh  
RUN chmod +x /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  
  
# Add startup file  
COPY supervisord.conf /etc/supervisor/supervisord.conf  
  
VOLUME /var/kippo  
  
EXPOSE 22  
  
# Start Kippo from supervisord on startup  
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/supervisord.conf"]  

