FROM ruby:2.4.2  
MAINTAINER Ronny Trommer <ronny@opennms.org>  
  
ARG FRAB_VERSION=v0.6  
ARG FRAB_HOME=/opt/frab  
ARG NGINX_LOG=/var/log/nginx  
  
LABEL vendor="frab" \  
org.frab.version="${FRAB_VERSION}" \  
org.frab.license="MIT License"  
  
# Install dependencies for rails app frab and update the system  
RUN apt-get update && \  
apt-get -y upgrade && \  
gem install bundler --no-ri --no-rdoc && \  
gem install passenger && \  
passenger-install-nginx-module --auto --auto-download --prefix=/opt/nginx
--languages ruby && \  
mkdir -p ${NGINX_LOG} && \  
curl -sL https://deb.nodesource.com/setup_7.x | bash - && \  
apt-get -y install nodejs  
  
# Get frab from GitHub repo and compile for production environment including
database drivers  
RUN git clone https://github.com/frab/frab.git ${FRAB_HOME} && \  
cd ${FRAB_HOME} && \  
git checkout -b ${FRAB_VERSION} tags/${FRAB_VERSION} && \  
gem install bundler --conservative && \  
gem install exception_notification && \  
bundle check || bundle install && \  
cp config/database.yml.template config/database.yml && \  
rm -f log/* && \  
rm -rf tmp/cache  
  
# Use entrypoint script to run the rails server and the nginx proxy  
COPY ./docker-entrypoint.sh /  
COPY ./assets/nginx.conf /opt/nginx/conf/nginx.conf  
  
WORKDIR ${FRAB_HOME}  
  
VOLUME [ "/opt/frab/db", "/opt/frab/app/public" ]  
  
CMD [ "/docker-entrypoint.sh" ]  
  
EXPOSE 80  

