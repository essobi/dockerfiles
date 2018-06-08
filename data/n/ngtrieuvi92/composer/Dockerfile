FROM composer/composer:base  
MAINTAINER Vi Nguyen <vi.nt@geekup.vn>  
  
ENV COMPOSER_VERSION 1.2.0  
# Install Composer  
RUN php /tmp/composer-setup.php --no-ansi --install-dir=/usr/local/bin
--filename=composer --version=${COMPOSER_VERSION} && rm -rf /tmp/composer-
setup.php  
  
# Setup to run with UID of non-root user  
RUN apt-get update && apt-get -y --no-install-recommends install \  
ca-certificates \  
curl  
  
RUN gpg --keyserver ha.pool.sks-keyservers.net --recv-keys
B42F6819007F00F88E364FD4036A9C25BF357DD4  
RUN curl -o /usr/local/bin/gosu -SL
"https://github.com/tianon/gosu/releases/download/1.4/gosu-$(dpkg --print-
architecture)" \  
&& curl -o /usr/local/bin/gosu.asc -SL
"https://github.com/tianon/gosu/releases/download/1.4/gosu-$(dpkg --print-
architecture).asc" \  
&& gpg --verify /usr/local/bin/gosu.asc \  
&& rm /usr/local/bin/gosu.asc \  
&& chmod +x /usr/local/bin/gosu  
  
COPY entrypoint.sh /usr/local/bin/entrypoint.sh  
RUN chmod +x /usr/local/bin/entrypoint.sh  
  
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]  
  
# Display version information.  
RUN composer --version  
  
CMD ["bash"]  

