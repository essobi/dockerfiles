FROM ruby:2.3.7-jessie  
  
RUN echo "deb http://deb.nodesource.com/node_8.x jessie main" >
/etc/apt/sources.list.d/nodesource.list && \  
echo "deb http://apt.postgresql.org/pub/repos/apt/ jessie-pgdg main" >
/etc/apt/sources.list.d/pgdg.list && \  
curl -sL https://deb.nodesource.com/gpgkey/nodesource.gpg.key | apt-key add -
&& \  
curl -sL https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add -  
  
RUN apt-get update -qq && apt-get install -qq -y --fix-missing --no-install-
recommends \  
apt-transport-https \  
build-essential \  
chrpath \  
libxft-dev \  
libfreetype6 \  
libfreetype6-dev \  
libfontconfig1 \  
libfontconfig1-dev \  
bsdmainutils \  
sqlite3 \  
gdal-bin \  
nodejs \  
libgdal-dev \  
lsb-release \  
python-gdal \  
postgresql-client-10 \  
wkhtmltopdf \  
xvfb \  
zip \  
unzip \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /var/tmp/* /tmp/*  
  
ENV BUNDLE_PATH /bundle_path  
  
WORKDIR /aim_gem  
RUN mkdir -p /aim_gem  
COPY Gemfile* /aim_gem/  
  
RUN bundle install --full-index --without development test  
  
COPY wkhtmltopdf.sh /usr/local/bin/  
RUN chmod a+x /usr/local/bin/wkhtmltopdf.sh  
RUN ln -s /usr/local/bin/wkhtmltopdf.sh /usr/bin/wkhtmltopdf.sh  
  
COPY docker-entrypoint.sh /usr/local/bin/  
RUN chmod +x /usr/local/bin/docker-entrypoint.sh  
RUN ln -s /usr/local/bin/docker-entrypoint.sh /usr/bin/docker-entrypoint.sh  
  
ENTRYPOINT ["docker-entrypoint.sh"]  

