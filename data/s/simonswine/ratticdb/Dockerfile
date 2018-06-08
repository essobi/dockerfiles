FROM ubuntu:precise  
  
# Install dependencies  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get -y install unzip python python-pip \  
python-dev gcc libsqlite3-dev libcurl4-openssl-dev libldap2-dev \  
libsasl2-dev libxml2-dev libxslt-dev apache2 libapache2-mod-wsgi mysql-server
\  
supervisor libmysqlclient-dev && \  
apt-get clean && \  
rm /var/lib/apt/lists/*_*  
  
# Download rattic  
ENV RATTIC_VERSION 1.2.2  
ADD https://github.com/tildaslash/RatticWeb/archive/v${RATTIC_VERSION}.tar.gz
/opt/rattic.tar.gz  
  
# Unpack rattic  
RUN mkdir -p /opt/rattic && tar xvfz /opt/rattic.tar.gz -C /opt/rattic
--strip-components=1  
  
# Copy config  
ADD ./local.dist.cfg /opt/rattic/conf/local.dist.cfg  
RUN ln -s ../../../srv/rattic/conf/local.cfg /opt/rattic/conf/local.cfg  
ADD ./rattic.conf /etc/apache2/sites-available/rattic  
RUN ln -s ../../../srv/apache.conf /etc/apache2/sites-enabled/rattic  
# Install dependencies  
RUN cd /opt/rattic/ && pip install -r requirements-mysql.txt  
  
# Copy run script  
ADD ./run.sh /run.sh  
RUN chmod 755 /run.sh  
  
# Copy supervisor config  
ADD ./apache.foreground.sh /etc/apache2/foreground.sh  
ADD ./supervisord.apache.conf /etc/supervisor/conf.d/apache.conf  
ADD ./supervisord.mysql.conf /etc/supervisor/conf.d/mysql.conf  
  
# Expose http port  
EXPOSE 80  
# Default command  
CMD ["/run.sh"]  
  
VOLUME /srv  

