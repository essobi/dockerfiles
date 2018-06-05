FROM ruby:2.3.1-slim  
MAINTAINER Gordon Chan <github.com/gchan>  
  
# Install postgres-client-9.5  
RUN apt-key adv --keyserver ha.pool.sks-keyservers.net --recv-keys
B97B0AFCAA1A47F044F244A07FCC7D46ACCC4CF8  
  
RUN echo 'deb http://apt.postgresql.org/pub/repos/apt/ jessie-pgdg main' 9.5 >
/etc/apt/sources.list.d/pgdg.list  
  
RUN apt-get update && apt-get install -qq -y build-essential wget cron
postgresql-client-9.5 --fix-missing --no-install-recommends  
  
RUN gem install backup whenever  
  
ENV INSTALL_PATH /backup  
RUN mkdir -p $INSTALL_PATH  
WORKDIR $INSTALL_PATH  
  
COPY . $INSTALL_PATH  
  
RUN touch /var/log/cron.log  
  
ENTRYPOINT ["/backup/entrypoint.sh"]  
  
CMD cron && tail -F /var/log/cron.log  

