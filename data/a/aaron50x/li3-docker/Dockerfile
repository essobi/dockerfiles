FROM php:5  
RUN apt-get update -y && \  
apt-get install -y git-core unzip pkg-config libssl-dev  
RUN useradd --uid 1000 -d /home/li3 li3 && \  
mkdir -p /home/li3/app && \  
chown 1000:1000 -R /home/li3 && \  
pecl install mongo && \  
echo "extension=mongo.so" > /usr/local/etc/php/conf.d/add_mongo.ini && \  
echo "error_reporting = E_ALL\nshort_open_tag = Off" >
/usr/local/etc/php/conf.d/li3_recommended.ini && \  
curl https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin
--filename composer  
WORKDIR /home/li3/app  
VOLUME /home/li3/app  

