FROM ubuntu:zesty  
MAINTAINER Natanael Arndt <arndtn@gmail.com>  
  
ENV LANG C.UTF-8  
ENV SSH_AUTH_SOCK /var/run/ssh-agent.sock  
  
# Install  
## zlib1g-dev is needed for nokogiri dependency of jekyll-rdf  
## ruby-dev and build-essential are needed to build jekyll  
RUN apt-get update && apt-get install -y \  
git \  
ruby \  
ruby-dev \  
build-essential \  
nginx \  
uwsgi \  
supervisor \  
zlib1g-dev \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN gem install --no-rdoc --no-ri jekyll bundler  
  
# Configure nginx.  
RUN echo "\ndaemon off;" >> /etc/nginx/nginx.conf  
  
# Add configuration files.  
ADD ./nginx.conf /etc/nginx/sites-enabled/default  
ADD ./uwsgi.ini /data/uwsgi/uwsgi.ini  
ADD ./supervisor-app.conf /etc/supervisor/conf.d/  
  
# Add the script used to kick off the jekyll build.  
ADD ./buildsite.sh /data/cgi/buildsite.sh  
RUN chmod +x /data/cgi/buildsite.sh  
  
VOLUME /data/jekyll/source  
  
EXPOSE 80  
CMD ["supervisord", "-n"]  

