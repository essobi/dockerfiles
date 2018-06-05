FROM ubuntu:16.04  
MAINTAINER Dmitry Mozzherin  
ENV LAST_FULL_REBUILD 2016-08-06  
RUN apt-get update && \  
apt-get install -y software-properties-common && \  
apt-add-repository ppa:brightbox/ruby-ng && \  
apt-get update && \  
apt-get install -y ruby2.3 ruby2.3-dev \  
zlib1g-dev liblzma-dev libxml2-dev libpq-dev nodejs \  
libqt4-dev libqtwebkit-dev libmysqlclient-dev csh git \  
libxslt-dev supervisor build-essential supervisor && \  
add-apt-repository -y ppa:nginx/stable && \  
apt-get update && \  
apt-get install -qq -y nginx && \  
echo "\ndaemon off;" >> /etc/nginx/nginx.conf && \  
chown -R www-data:www-data /var/lib/nginx && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN locale-gen en_US.UTF-8  
  
ENV DISPLAY :99.0  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
ENV RACK_ENV development  
ENV RESQUE_WORKERS 1  
ENV QUEUE NameFinder  
ENV PUMA_WORKERS 1  
RUN echo 'gem: --no-rdoc --no-ri >> "$HOME/.gemrc"'  
  
RUN gem install bundler && \  
mkdir /app  
  
WORKDIR /app  
  
COPY config/docker/nginx-sites.conf /etc/nginx/sites-enabled/default  
COPY Gemfile /app  
COPY Gemfile.lock /app  
RUN bundle install  
  
RUN apt-get update && apt-get install -y xvfb  
RUN Xvfb :99 -ac -screen 0 $XVFB_WHD -nolisten tcp &  
  
COPY . /app  
  
CMD ["supervisord", "-c", "/app/config/docker/supervisord_dev.conf]  
  

