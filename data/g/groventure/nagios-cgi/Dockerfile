FROM groventure/nagios-base:debian-jessie  
MAINTAINER Hellyna NG <hellyna@groventure.com>  
  
RUN export DEBIAN_FRONTEND='noninteractive' && \  
apt-get update && \  
apt-get install --no-install-recommends -y \  
openssl \  
nagios3-cgi && \  
rm -f /etc/apache2/sites-enabled/* && \  
echo \  
'DocumentRoot /usr/share/nagios3/htdocs' \  
>> /etc/apache2/apache2.conf && \  
echo \  
'ServerName {{ server_name }}' \  
>> /etc/apache2/apache2.conf && \  
find /etc/apache2 -name '*.conf' -type f -print0 | \  
xargs -0 \  
sed -ri \  
's/^(\s*CustomLog)\s+\S+/\1 \/proc\/self\/fd\/1/g' && \  
find /etc/apache2 -name '*.conf' -type f -print0 | \  
xargs -0 \  
sed -ri \  
's/^(\s*ErrorLog)\s+\S+/\1 \/proc\/self\/fd\/2/g' && \  
sed -ri \  
's/^(url_html_path=).+$/\1\//g' \  
/etc/nagios3/cgi.cfg && \  
# sed -ri \  
# 's/^(ScriptAlias\s+\/cgi-bin)\/nagios3\s+(\S+)$/\1 \2/g' \  
# /etc/nagios3/apache2.conf && \  
sed -ri \  
's/^(\s*ScriptAlias\s+)\/nagios3(\/cgi-bin)(\s+\S+)\s*$/\1\2\3/g' \  
/etc/nagios3/apache2.conf && \  
sed -ri \  
's/^(\s*Alias\s+)\/nagios3(\/stylesheets)(\s+\S+)\s*$/\1\2\3/g' \  
/etc/nagios3/apache2.conf && \  
# sed -ri \  
# 's/^Alias\s+\/nagios3\s+(\S+)$/Alias \/ \1/g' \  
# /etc/nagios3/apache2.conf && \  
apt-get autoremove -y && \  
apt-get clean -y && \  
rm -rvf /var/lib/apt/lists/* && \  
rm -rvf /var/tmp/* && \  
rm -rvf /tmp/*  
  
COPY entrypoint.sh /usr/local/bin/entrypoint.sh  
  
ENTRYPOINT ["/bin/bash", "/usr/local/bin/entrypoint.sh"]  
  
EXPOSE 80/tcp  

