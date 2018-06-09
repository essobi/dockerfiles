FROM ubuntu:16.04  
MAINTAINER Manuel VACELET <manuel.vacelet@enalean.com>  
  
RUN apt-get update -y && \  
apt-get install -y curl php-cli nodejs npm ruby-sass jing trang git
libfontconfig gosu && \  
npm install -g less recess grunt-cli bower && \  
gem install scss-lint && \  
ln -s /usr/bin/nodejs /usr/bin/node && \  
rm -rf /var/lib/apt/lists/*  
  
RUN curl -o /usr/local/bin/phpab -fsSL "http://phpab.net/phpab-1.16.1.phar" &&
\  
chmod +x /usr/local/bin/phpab  
  
COPY run.sh /run.sh  
COPY run-as-owner.sh /run-as-owner.sh  
RUN chmod a+x /run.sh /run-as-owner.sh  
  
ENTRYPOINT ["/run.sh"]  

