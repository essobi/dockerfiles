FROM jaitaiwan/dockerfiles:composer  
  
# Install zip & posix  
RUN docker-php-ext-install zip  
  
RUN echo 'deb http://ftp.au.debian.org/debian testing main contrib' >>
/etc/apt/sources.list && \  
apt-get update  
  
# Install YAML  
RUN apt-get install -y libyaml-dev && \  
pecl install yaml && \  
echo 'extension=yaml.so' > $PHP_INI_DIR/conf.d/yaml.ini  
  
# Install ssh2  
RUN apt-get install -y libssh2-1-dev && \  
pecl install ssh2-0.12 && \  
echo 'extension=ssh2.so' > $PHP_INI_DIR/conf.d/ssh2.ini  
  
RUN rm -r /var/lib/apt/lists/*  
  
ENV PROVENDER_BIN $COMPOSER_HOME/vendor/bin/provender  
ENV PROVENDER_INSTALL_BIN $COMPOSER_HOME/vendor/bin/provender-install  
RUN composer global require centricwebestate/provender:dev-
master#c4f2e987b56afece6d8c8aff07cf73db3820aa85  
RUN export PATH=~/.composer/vendor/bin:$PATH  
  
ENTRYPOINT ["/root/.composer/vendor/bin/provender"]  
CMD ["-"]  

