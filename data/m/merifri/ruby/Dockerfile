FROM ruby:2.4.2  
  
RUN echo "deb http://apt.postgresql.org/pub/repos/apt/ jessie-pgdg main" >
/etc/apt/sources.list.d/pgdg.list && \  
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key
add \- && \  
curl -sL https://deb.nodesource.com/setup_8.x | bash - && \  
apt-get update -qq && \  
apt-get install -y libpq5 libpq-dev postgresql-client-10 nodejs locales \  
python-pip python-dev groff  
  
RUN echo "en_US.UTF-8 UTF-8" > /etc/locale.gen && locale-gen  
ENV LC_ALL en_US.utf8  
  
CMD [ "irb" ]  

