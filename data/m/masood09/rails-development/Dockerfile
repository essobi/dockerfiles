FROM ruby:2.3.1-slim  
  
MAINTAINER Masood Ahmed "masood.ahmed@galepartners.com"  
EXPOSE 3000  
ENV HOME /root  
ENV APP_HOME /application/  
  
RUN echo "gem: --no-rdoc --no-ri" > $HOME/.gemrc  
  
RUN apt-get update && \  
apt-get install -y --no-install-recommends build-essential \  
apt-transport-https \  
ca-certificates \  
gnupg \  
curl \  
git \  
imagemagick \  
libpq-dev \  
libxml2-dev \  
libxslt1-dev \  
openssh-client \  
libsqlite3-dev \  
sqlite3 \  
file \  
libmysqlclient-dev  
  
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash -  
RUN apt-get install -y --no-install-recommends nodejs  
RUN ln -sf /usr/bin/nodejs /usr/local/bin/node  
RUN npm install -g phantomjs-prebuilt  
  
RUN gem install bundler --no-rdoc --no-ri  
RUN gem install rubocop --no-rdoc --no-ri  
RUN gem install rails -v 4.2.6 --no-rdoc --no-ri  
  
# Clean up APT and bundler when done.  
RUN rm -rf /usr/share/doc \  
/usr/share/man \  
/usr/share/groff \  
/usr/share/info \  
/usr/share/lintian \  
/usr/share/linda \  
/usr/share/locale/ \  
/var/cache/man  
  
# Clean up APT when done.  
RUN apt-get clean  
RUN apt-get autoclean  
RUN apt-get autoremove  
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Install bundle of gems  
RUN mkdir -p $APP_HOME  
WORKDIR $APP_HOME  
  
CMD ["tail", "-f", "/dev/null"]  

