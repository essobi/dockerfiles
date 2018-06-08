FROM ruby:2.2.0  
MAINTAINER Kazuki Fukui  
  
RUN apt-get update && \  
apt-get install -y --no-install-recommends wget nodejs sqlite3 libicu-dev
cmake && \  
apt-get -y autoremove && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
# download lodge  
ENV LODGE_VERSION 0.11.2  
RUN wget --no-check-certificate
https://github.com/lodge/lodge/archive/v${LODGE_VERSION}.tar.gz && \  
tar xf v${LODGE_VERSION}.tar.gz && \  
rm -rf v${LODGE_VERSION}.tar.gz && \  
ln -s /lodge-${LODGE_VERSION} lodge  
WORKDIR /lodge  
RUN gem install bundler  
  
# configure database  
COPY database.yml ./config/database.yml  
  
# copy script for entrypoint  
COPY entrypoint.sh ./start_lodge.sh  
  
RUN bundle install --clean --quiet --path vendor/bundle && \  
sed -ie 's/serve_static_assets/serve_static_files/' \  
./config/environments/production.rb && \  
mkdir /lodge/tmp/ && \  
chmod 775 ./start_lodge.sh  
  
# set env  
ENV DELIVERY_METHOD smtp  
ENV SMTP_PORT 587  
ENV SMTP_AUTH_METHOD plain  
ENV SMTP_ENABLE_STARTTLS_AUTO true  
ENV LODGE_THEME lodge  
  
VOLUME /lodge/log  
VOLUME /db  
EXPOSE 3000  
CMD ./start_lodge.sh  

