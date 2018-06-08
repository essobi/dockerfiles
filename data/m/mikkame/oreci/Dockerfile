FROM heroku/cedar:14  
MAINTAINER mikka.me  
RUN apt-get update  
RUN apt-get install -y --force-yes build-essential curl git zlib1g-dev libssl-
dev libreadline-dev libyaml-dev libxml2-dev libxslt-dev  
RUN git clone https://github.com/sstephenson/rbenv.git /root/.rbenv  
RUN git clone https://github.com/sstephenson/ruby-build.git
/root/.rbenv/plugins/ruby-build  
RUN ./root/.rbenv/plugins/ruby-build/install.sh  
ENV PATH /root/.rbenv/bin:$PATH  
RUN echo 'eval "$(rbenv init -)"' >> /etc/profile.d/rbenv.sh # or /etc/profile  
RUN echo 'eval "$(rbenv init -)"' >> .bashrc  
ENV CONFIGURE_OPTS --disable-install-doc  
RUN rbenv install $(rbenv install -l | grep -v - | tail -1)  
RUN rbenv global $(rbenv install -l | grep -v - | tail -1)  
RUN adduser oreci  
ENV PATH
/root/.rbenv/shims:/root/.rbenv/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin  
  
  
#for ruby  
RUN echo $PATH  
RUN gem i rails_best_practices  
RUN gem i reek  
RUN gem i brakeman  
RUN gem i bundler  
  
RUN apt-get install -y php5  
RUN apt-get install -y npm  
RUN ln -s /usr/bin/nodejs /usr/bin/node  
WORKDIR /home/oreci  
RUN php -r "readfile('https://getcomposer.org/installer');" > composer-
setup.php  
RUN php -r "if (hash('SHA384', file_get_contents('composer-setup.php')) ===
'fd26ce67e3b237fffd5e5544b45b0d92c41a4afe3e3f778e942e43ce6be197b9cdc7c251dcde6e2a52297ea269370680')
{ echo 'Installer verified'; } else { echo 'Installer corrupt';
unlink('composer-setup.php'); }"  
RUN php composer-setup.php  
  
USER oreci  
  
  
#for PHP  
RUN curl -OL https://squizlabs.github.io/PHP_CodeSniffer/phpcs.phar  
RUN curl -OL https://static.phpmd.org/php/2.3.2/phpmd.phar  
  
#for node  
RUN npm install jshint  
RUN npm install eslint  
RUN npm install coffeelint  
RUN npm install tslint  
RUN npm install scss-lint  
  
CMD mkdir -m 700 .ssh  
CMD ssh-keygen -t rsa -b 2048 -N "" -f .ssh/id_rsa  
CMD echo eval "echo \"#################\";echo .ssh/id_rsa.pub;echo
\"#################\";"

