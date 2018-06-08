FROM debian:jessie  
  
ADD localhost.conf /etc/apache2/sites-available/localhost.conf  
ADD localhost-ssl.conf /etc/apache2/sites-available/localhost-ssl.conf  
  
RUN apt-get update -y \  
&& apt-get install -y \  
apache2 \  
curl \  
gcc \  
libxml2-dev \  
libssl-dev \  
libexpat1-dev \  
make \  
mysql-client \  
zip \  
&& curl -L https://cpanmin.us | perl - App::cpanminus \  
&& cpanm \  
Plack \  
CGI::PSGI \  
CGI::Parse::PSGI \  
XMLRPC::Transport::HTTP::Plack \  
Imager \  
IPC::Run \  
Crypt::DSA \  
Crypt::SSLeay \  
XML::SAX::ExpatXS \  
XML::LibXML::SAX \  
Archive::Zip \  
Web::Scraper \  
Net::SMTP::SSL \  
Net::SMTP::TLS \  
&& sed -i \  
-e 's/ServerTokens OS/ServerTokens ProductOnly/g' \  
-e 's/ServerSignature On/ServerSignature Off/g' \  
/etc/apache2/conf-available/security.conf \  
&& sed -i \  
-e '/Listen 443$/i \ \ \ \ NameVirtualHost *:443' \  
/etc/apache2/ports.conf \  
&& mkdir /var/www/htdocs \  
&& a2enmod cgid \  
&& a2enmod ssl \  
&& a2dissite 000-default \  
&& a2ensite localhost \  
&& a2ensite localhost-ssl \  
&& apt-get autoclean  
  
EXPOSE 80 443  
CMD ["/usr/sbin/apache2ctl","-DFOREGROUND"]  

