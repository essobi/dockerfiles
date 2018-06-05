#  
# branched Nasqueron - Phabricator image  
#  
FROM nasqueron/nginx-php-fpm  
  
  
#  
# Prepare the container  
#  
RUN apt-get update && apt-get install -y \  
mercurial subversion python-pygments openssh-client imagemagick \  
mysql-client \  
\--no-install-recommends && rm -r /var/lib/apt/lists/*  
  
RUN cd /opt && \  
git clone https://github.com/phacility/libphutil.git && \  
git clone https://github.com/phacility/arcanist.git && \  
git clone https://github.com/phacility/phabricator.git && \  
mkdir -p /var/tmp/phd && \  
chown app:app /var/tmp/phd  
  
COPY files /  
  
#  
# Docker properties  
#  
VOLUME ["/opt/phabricator/conf/local", "/var/repo", "/var/files"]  
  
WORKDIR /opt/phabricator  
CMD ["/usr/local/sbin/init-container"]  

