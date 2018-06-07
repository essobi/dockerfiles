FROM ruby:2.4  
MAINTAINER Bjoern Stierand <bjoern-github@innovention.de>  
LABEL version="0.4"  
LABEL description="Docker image for sifttter-redux-known"  
  
# install sifttter-redux-known  
RUN ["/usr/bin/git", "clone", "https://github.com/egoexpress/sifttter-redux-
known.git"]  
WORKDIR "/sifttter-redux-known"  
RUN ["/usr/local/bin/gem", "build", "sifttter-redux-known.gemspec"]  
RUN ["/usr/local/bin/gem", "install", "sifttter-redux-known-1.0.gem"]  
  
# install Dropbox-Uploader  
RUN mkdir /usr/local/opt  
WORKDIR "/usr/local/opt"  
RUN ["/usr/bin/git", "clone", "https://github.com/andreafabrizi/Dropbox-
Uploader.git"]  
  
# prepare base config for sifttter-redux-known  
COPY files/sifttter_redux.yaml /root/.sifttter_redux  
RUN mkdir /tmp/sifttter-redux-known && mkdir /tmp/sifttter  
  
# change default encoding to UTF-8 and install cron  
RUN apt-get update && \  
apt-get install -yq --no-install-recommends locales cron && \  
echo "en_US.UTF-8 UTF-8" > /etc/locale.gen && \  
locale-gen  
  
COPY files/bashrc /root/.bashrc  
COPY files/crontab /etc/crontab  
WORKDIR "/"  
  
# setup entrypoint  
COPY files/docker-entrypoint.sh /docker-entrypoint.sh  
RUN chmod 555 /docker-entrypoint.sh  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
COPY files/srd_run /usr/bin/srd_run  
RUN chmod 755 /usr/bin/srd_run  
CMD ["/usr/bin/srd_run"]  

