FROM ubuntu:14.04  
RUN \  
apt-get -qq update && \  
apt-get -y install \  
apache2 \  
dpkg-dev \  
git \  
graphviz \  
php5 \  
php5-cli \  
php5-curl \  
php5-dev \  
php5-gd \  
php5-json \  
php5-ldap \  
php5-mysql \  
php-apc \  
python-pygments \  
&& \  
apt-get -y clean && \  
rm -rf /var/lib/apt/lists/*  
  
RUN \  
mkdir /usr/local/phabricator && \  
cd /usr/local/phabricator && \  
git clone https://github.com/phacility/libphutil.git && \  
(cd libphutil && git checkout b4f38af384807b7dcd1e3d1a96e9e9069e4d6964) &&\  
git clone https://github.com/phacility/arcanist.git && \  
(cd arcanist && git checkout 3d7ac867f53892b8210339bbb0c5fd91e0e36d78) &&\  
git clone https://github.com/phacility/phabricator.git && \  
(cd phabricator && git checkout 3493d9d5138e0a630624bced548090163ce9be8a)  
  
ADD apache.conf /etc/apache2/sites-available/phabricator.conf  
  
RUN \  
a2enmod rewrite && \  
a2ensite phabricator && \  
a2dissite 000-default  
  
ADD start /usr/local/phabricator/start  
  
VOLUME /var/repo  
VOLUME /usr/local/phabricator/phabricator/conf/local  
  
CMD ["/usr/local/phabricator/start"]  
EXPOSE 80  

