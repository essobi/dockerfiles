FROM debian:jessie  
MAINTAINER Dmitry Shapovalov  
  
ARG hostuid=969  
ARG hostgid=969  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV RUN_USER mercurial  
ENV RUN_GROUP mercurial  
ENV RUN_PORT 8009  
ENV APACHE_RUN_USER $RUN_USER  
ENV APACHE_RUN_GROUP $RUN_GROUP  
  
COPY . /tmp  
  
# Install packages  
RUN apt-get update && \  
apt-get install --assume-yes \  
apache2 \  
mercurial \  
tk \  
vim && \  
apt-get clean  
  
# Create user and group  
RUN groupadd -g $hostgid $RUN_GROUP && \  
useradd -u $hostuid -g $hostgid -M $RUN_USER  
  
# Create files and folders for mercurial  
RUN mkdir /mercurial && \  
mkdir /mercurial/repositories && \  
mkdir /mercurial/scripts && \  
touch /mercurial/users && \  
mkdir /mercurial/logs && \  
mkdir /mercurial/backups && \  
chown -R $RUN_USER:$RUN_GROUP /mercurial  
  
# Configure apache  
RUN sed -i 's|:80>|:'"$RUN_PORT"'>|' /etc/apache2/sites-
available/000-default.conf && \  
sed -i 's|#ServerName www.example.com|ServerName localhost|'
/etc/apache2/sites-available/000-default.conf && \  
mv /tmp/mercurial.conf /etc/apache2/sites-available && \  
sed -i 's|Listen 80|Listen '"$RUN_PORT"'|' /etc/apache2/ports.conf && \  
echo "ServerName localhost" > /etc/apache2/conf-available/servername.conf && \  
a2enconf servername && \  
a2enmod cgi && \  
a2ensite mercurial && \  
rm -rf /var/log/apache2 && \  
ln -s /mercurial/logs /var/log/apache2 && \  
chown -h $RUN_USER:$RUN_GROUP /var/log/apache2 && \  
mkdir -p /var/lock/apache2 && \  
chown -R $RUN_USER:$RUN_GROUP /var/lock/apache2 && \  
mkdir -p /var/run/apache2 && \  
chown -R $RUN_USER:$RUN_GROUP /var/run/apache2  
  
# Configure mercurial  
RUN mv /tmp/hgrc /etc/mercurial && \  
mv /tmp/hgweb.config /mercurial && \  
chown $RUN_USER:$RUN_GROUP /mercurial/hgweb.config && \  
sed 's|config = ".*"|config = "/mercurial/hgweb.config"|'
/usr/share/doc/mercurial/examples/hgweb.cgi > /mercurial/hgweb.cgi && \  
chmod a+x /mercurial/hgweb.cgi  
  
# Configure helper scripts  
RUN mv /tmp/startup /mercurial/scripts && \  
chmod a+x /mercurial/scripts/startup && \  
mv /tmp/shutdown /mercurial/scripts && \  
chmod a+x /mercurial/scripts/shutdown && \  
mv /tmp/createrepositoryhgrc /mercurial/scripts && \  
chmod a+x /mercurial/scripts/createrepositoryhgrc && \  
mv /tmp/backup /mercurial/scripts && \  
chmod a+x /mercurial/scripts/backup && \  
mv /tmp/restore /mercurial/scripts && \  
chmod a+x /mercurial/scripts/restore  
  
USER $RUN_USER  
  
EXPOSE $RUN_PORT  
  
ENTRYPOINT ["/mercurial/scripts/startup"]  

