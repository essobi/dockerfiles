FROM ruby:2.3-stretch  
  
#  
### Sources  
#  
# Required for elasticsearch sources. Reference:  
# https://www.elastic.co/guide/en/elasticsearch/reference/5.6/deb.html#deb-
repo  
RUN apt-get update && apt-get -y --no-install-recommends install apt-
transport-https  
  
# Elasticsearch  
RUN wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | apt-key
add - \  
&& echo 'deb https://artifacts.elastic.co/packages/5.x/apt stable main' | tee
/etc/apt/sources.list.d/elastic-5.x.list  
  
# NodeJS  
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash -  
  
# PostgreSQL  
RUN echo 'deb http://apt.postgresql.org/pub/repos/apt/ stretch-pgdg main' >
/etc/apt/sources.list.d/postgresql.list \  
&& wget --no-check-certificate -q
https://www.postgresql.org/media/keys/ACCC4CF8.asc -O- | apt-key add -  
  
# Yarn  
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - \  
&& echo 'deb https://dl.yarnpkg.com/debian/ stable main' | tee
/etc/apt/sources.list.d/yarn.list  
  
#  
### Dependencies  
#  
RUN apt-get update && apt-get -y --no-install-recommends install \  
sudo \  
elasticsearch \  
jpegoptim \  
nodejs \  
openjdk-8-jdk \  
postgresql-9.5 \  
redis-server \  
memcached \  
yarn  
  
# npm upgrading workaround. Reference:  
# https://stackoverflow.com/questions/46113900/npm-breaks-after-it-has-been-
upgraded-in-docker-container  
RUN npm uninstall npm -g  
RUN yarn global add npm@5.6.0  
  
COPY entrypoint.sh /entrypoint.sh  
  
CMD ["/entrypoint.sh"]  

