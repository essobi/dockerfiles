FROM outfound/appserver  
  
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash -  
  
RUN apt-get -y install \  
bzip2 \  
git \  
zip \  
jq \  
wget \  
sudo \  
nodejs \  
&& apt-get clean all \  
&& echo -n "Node Version is: " \  
&& node --version \  
&& echo -n "NPM Version is: " \  
&& npm --version  
  
# Nuke node (Amateur Packet Radio Node Program) and replace with nodejs  
RUN sudo apt-get -y --purge remove node && \  
update-alternatives --install /usr/bin/node node /usr/bin/nodejs 10  
  
# Node and NPM - Bower, Gulp, etc.  
RUN npm install -g bower gulp  
  
# PHPUnit  
RUN wget "https://phar.phpunit.de/phpunit.phar" -O /usr/bin/phpunit && chmod
+x /usr/bin/phpunit  
  
RUN addgroup --gid 6855 outfound && \  
yes '' | adduser --disabled-password \  
outfound --ingroup \  
outfound  
  
# SUDO  
RUN echo 'outfound ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers && \  
sed -i 's/requiretty/!requiretty/' /etc/sudoers  
  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin/ --filename=composer  

