FROM ruby  
  
# install SASS & Compass, see https://www.drupal.org/node/2188263  
RUN gem install compass --version 0.12.7  
# ssh, sftp are for automatically uploading generated css files to remote  
RUN gem install net-ssh net-sftp  
  
WORKDIR /usr/src/app  
  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update -qq && apt-get install -y locales -qq && locale-gen
en_US.UTF-8 en_us && dpkg-reconfigure locales && dpkg-reconfigure locales &&
locale-gen C.UTF-8 && /usr/sbin/update-locale LANG=C.UTF-8 && rm -rf
/var/lib/apt/lists/*  
ENV LANG C.UTF-8  
ENV LANGUAGE C.UTF-8  
ENV LC_ALL C.UTF-8  

