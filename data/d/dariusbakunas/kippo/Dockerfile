FROM debian:wheezy  
MAINTAINER Darius Bakunas-Milanowski <bakunas@gmail.com>  
  
RUN apt-get update -yqq && apt-get install -yqq \  
authbind \  
dos2unix \  
git \  
mysql-client \  
openssl \  
python-dev \  
python-mysqldb \  
python-openssl \  
python-pyasn1 \  
python-twisted \  
supervisor  
  
# add kippo user that can't login  
RUN useradd -r -s /bin/false kippo && \  
  
# install kippo to /opt/kippo  
mkdir /opt/kippo/ && \  
git clone https://github.com/micheloosterhof/kippo.git /opt/kippo/ && \  
cp /opt/kippo/kippo.cfg.dist /opt/kippo/kippo.cfg && \  
  
# set up log dirs  
mkdir -p /var/kippo/dl /var/kippo/log/tty /var/run/kippo && \  
  
# delete old dirs to prevent confusion  
rm -rf /opt/kippo/dl && \  
  
# set up permissions  
chown -R kippo:kippo /opt/kippo/ && chown -R kippo:kippo /var/run/kippo/ && \  
  
# allow binding to 22 port  
touch /etc/authbind/byport/22 && chown kippo /etc/authbind/byport/22 && chmod
777 /etc/authbind/byport/22  
# add config for supervisord  
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
COPY entrypoint.sh /entrypoint.sh  
  
RUN chown -R kippo:kippo /var/kippo && \  
chmod +x /entrypoint.sh  
  
VOLUME /var/kippo  
  
EXPOSE 22  
ENTRYPOINT ["/entrypoint.sh"]  
  
# start supervisor on launch  
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/supervisord.conf"]  

