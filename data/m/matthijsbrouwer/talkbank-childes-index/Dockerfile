# Ubuntu - Demo index subset Childes  
FROM ubuntu:16.04  
MAINTAINER Matthijs Brouwer  
  
EXPOSE 80  
ENV SOLR_VERSION 7.1.0  
ENV MTAS_VERSION 7.1.0.1  
USER root  
  
RUN mkdir /data && \  
mkdir /data/solr && \  
mkdir /data/solr/lib && \  
mkdir /data/resources && \  
mkdir /data/composer  
  
ADD
http://central.maven.org/maven2/nl/knaw/meertens/mtas/mtas/$MTAS_VERSION/mtas-$MTAS_VERSION.jar
/data/solr/lib/  
  
WORKDIR "/data"  
  
RUN apt-get update && apt-get install -y locales lsof software-properties-
common && \  
locale-gen en_US.UTF-8 en_US && update-locale LANG=en_US.UTF-8
LANGUAGE=en_US:en  
  
RUN add-apt-repository -y ppa:webupd8team/java && \  
apt-get update && \  
echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true |
/usr/bin/debconf-set-selections && \  
apt-get install -y oracle-java8-installer  
  
RUN apt-get install -y wget unzip  
  
RUN cd /data/resources && \  
wget -e robots=off -r -l inf --no-remove-listing -nH --no-parent -P "data-xml"
\--cut-dirs=1 -R "index.html*" "http://childes.talkbank.org/data-xml/Celtic/"
&& \  
wget -e robots=off -r -l inf --no-remove-listing -nH --no-parent -P "data-xml"
\--cut-dirs=1 -R "index.html*" "http://childes.talkbank.org/data-xml/French/"  
  
RUN cd /data/resources && \  
find . -name "*.zip" | while read filename; do unzip -o -d "`dirname
"$filename"`" "$filename"; find data-xml -name "*\\.xml" -exec gzip {} \; ; rm
"$filename" ; done;  
  
RUN cd /data/resources && \  
wget -e robots=off -r -l inf --no-remove-listing -nH --no-parent -R
"index.html*" "http://alpha.talkbank.org/data-cmdi/childes-data.cmdi" && \  
wget -e robots=off -r -l inf --no-remove-listing -nH --no-parent -R
"index.html*" "http://alpha.talkbank.org/data-cmdi/childes-data/Celtic/"
"http://alpha.talkbank.org/data-cmdi/childes-data/Celtic.cmdi" && \  
wget -e robots=off -r -l inf --no-remove-listing -nH --no-parent -R
"index.html*" "http://alpha.talkbank.org/data-cmdi/childes-data/French/"
"http://alpha.talkbank.org/data-cmdi/childes-data/French.cmdi"  
  
RUN apt-get install -y python-software-properties apache2 php libapache2-mod-
php php-cli curl php-curl php-xml subversion  
  
RUN mathurl=$(curl -s
'http://www.apache.org/dyn/closer.lua/commons/math/binaries/commons-
math3-3.6.1-bin.tar.gz' | grep -o '<strong>[^<]*</strong>' | sed
's/<[^>]*>//g' | head -1) && \  
if echo "$mathurl" | grep -q '^.*[^ ].*$'; then \  
curl -f -o /data/solr/lib/commons-math3-3.6.1-bin.tar.gz -O $mathurl || true;
\  
fi && \  
if [ ! -f /data/solr/lib/commons-math3-3.6.1-bin.tar.gz ]; then \  
echo "Commons-math3 not found in mirror, falling back to apache archive"; \  
mathurl="http://archive.apache.org/dist/commons/math/binaries/commons-
math3-3.6.1-bin.tar.gz"; \  
curl -f -o /data/solr/lib/commons-math3-3.6.1-bin.tar.gz -O $mathurl; \  
fi && \  
cd /data/solr && \  
tar xzf lib/commons-math3-3.6.1-bin.tar.gz -C lib commons-math3-3.6.1/commons-
math3-3.6.1.jar --strip-components=1 && \  
rm lib/commons-math3-3.6.1-bin.tar.gz  
  
RUN solrurl=$(curl -s
"http://www.apache.org/dyn/closer.lua/lucene/solr/$SOLR_VERSION/solr-$SOLR_VERSION.tgz"
| grep -o '<strong>[^<]*</strong>' | sed 's/<[^>]*>//g' | head -1) && \  
if echo "$solrurl" | grep -q '^.*[^ ].*$'; then \  
curl -f -o /data/solr-$SOLR_VERSION.tgz -O $solrurl || true; \  
fi && \  
if [ ! -f /data/solr-$SOLR_VERSION.tgz ]; then \  
echo "Solr $SOLR_VERSION not found in mirror, falling back to apache archive";
\  
solrurl="http://archive.apache.org/dist/lucene/solr/$SOLR_VERSION/solr-$SOLR_VERSION.tgz";
\  
curl -f -o /data/solr-$SOLR_VERSION.tgz -O $solrurl; \  
fi && \  
tar xzf solr-$SOLR_VERSION.tgz solr-$SOLR_VERSION/bin/install_solr_service.sh
--strip-components=2 && \  
bash ./install_solr_service.sh solr-$SOLR_VERSION.tgz && rm
install_solr_service.sh && rm -rf solr-$SOLR_VERSION.tgz  
  
RUN service apache2 stop && \  
echo "ServerName localhost" | tee /etc/apache2/conf-available/fqdn.conf && \  
a2enmod proxy && \  
a2enmod proxy_http && \  
a2enmod proxy_ajp && \  
a2enmod rewrite && \  
a2enmod deflate && \  
a2enmod headers && \  
a2enmod proxy_balancer && \  
a2enmod proxy_connect && \  
a2enmod proxy_html && \  
a2enmod xml2enc && \  
a2enconf fqdn && \  
sed -i '/<\/VirtualHost>/ i ProxyPass /solr
http://localhost:8983/solr\nProxyPassReverse /solr http://localhost:8983/solr'
/etc/apache2/sites-enabled/000-default.conf && \  
sed -i '1s/^/<Directory \/var\/www\/>\n\tOptions Indexes FollowSymLinks
MultiViews\n\tAllowOverride All\n\tOrder allow,deny\n\tallow from
all\n<\/Directory>\n\n /' /etc/apache2/sites-enabled/000-default.conf && \  
rm -rf /var/www/html/* && \  
chmod -R 755 /var/www/html && \  
printf "echo\n" >> /start.sh && \  
printf "echo \"================== Mtas -- Demo index subset Childes
===================\"\n" >> /start.sh && \  
printf "echo \" Timestamp %s\"\n" "$(date)" >> /start.sh && \  
printf "echo \" Lucene/Solr version $SOLR_VERSION\"\n" >> /start.sh && \  
printf "echo \" Mtas release $MTAS_VERSION\"\n" >> /start.sh && \  
printf "echo
\"========================================================================\"\n"
>> /start.sh && \  
printf "echo\n" >> /start.sh && \  
printf "service solr start\nsleep 5\nservice apache2 start\n" >> /start.sh &&
\  
chmod 755 /start.sh  
  
RUN cd /var/www/html/ && \  
svn export
https://github.com/matthijsbrouwer/talkbank/trunk/docker/index/archive/
childes.talkbank.org  
  
RUN cd /data/solr/ && \  
svn export https://github.com/matthijsbrouwer/talkbank/trunk/index/solr/conf/
conf  
  
RUN cd /var/solr/data/ && mkdir childes && cd childes && \  
echo "name=childes" > core.properties && cp -a /data/solr/lib . && cp -a
/data/solr/conf . && cd conf && \  
sed -i 's/http:\/\/childes.talkbank.org\/data-orig-
xml\//http:\/\/localhost\/childes.talkbank.org\/data-orig-xml\//g' mtas.xml &&
\  
chmod -R 777 /var/solr/data/childes  
  
RUN service solr start && service apache2 start && sleep 5 && \  
svn export https://github.com/matthijsbrouwer/talkbank/trunk/index/scripts/
scripts && \  
cd scripts && \  
php create.php "http://alpha.talkbank.org/data-cmdi/childes-data.cmdi"
"childes" "http://localhost/solr/" "/data/resources/data-cmdi"  
  
RUN apt-get install -y php-curl php-sqlite3 php-mbstring && \  
cd /data/composer && wget -O installer https://getcomposer.org/installer && \  
php installer && mv composer.phar /usr/local/bin/composer && \  
cd /var/www/html && \  
svn export https://github.com/meertensinstituut/broker/trunk/src/ broker && \  
cd /var/www/html/broker && composer install && chmod 777
/var/www/html/broker/cache &&\  
cd /var/www/html/broker/config && \  
svn export
https://github.com/matthijsbrouwer/talkbank/trunk/docker/index/broker/config.inc.php  
  
CMD bash -C '/start.sh'; 'bash'  

