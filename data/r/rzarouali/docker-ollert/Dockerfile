FROM debian:wheezy  
  
MAINTAINER xinity <xinity77@gmail.com>  
  
# fix source bug  
RUN rm /bin/sh && ln -s /bin/bash /bin/sh  
  
# Add repo for mongo  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 7F0CEB10  
RUN echo "deb http://repo.mongodb.org/apt/debian wheezy/mongodb-org/3.0 main"
| tee /etc/apt/sources.list.d/mongodb-org-3.0.list  
  
# Install all apt packages  
RUN apt-get -qqy update && apt-get -y install mongodb-org libxslt-dev
libxml2-dev build-essential libqtwebkit-dev git zlib1g zlib1g-dev curl procps
locales  
  
# Copy environment file  
# Add repo for latest ruby  
RUN gpg --keyserver hkp://keys.gnupg.net --recv-keys
409B6B1796C275462A1703113804BB82D39DC0E3  
RUN curl -sSL https://get.rvm.io | bash -s stable --ruby=2.2.0  
  
WORKDIR /srv  
RUN git clone https://github.com/sep/ollert.git /srv/ollert  
#copy ./Gemfile /opt/app/ollert/Gemfile  
# Use rake to install ruby packages  
WORKDIR /srv/ollert  
RUN source /usr/local/rvm/scripts/rvm  
RUN /bin/bash -l -c "/usr/local/rvm/bin/rvm ruby-2.2.0"  
RUN echo "gem: --no-rdoc --no-ri" >> ~/.gemrc  
RUN /bin/bash -l -c "gem install bundler"  
RUN /bin/bash -l -c "bundle install --quiet"  
  
# Install program to configure locales  
RUN dpkg-reconfigure locales && \  
locale-gen C.UTF-8 && \  
/usr/sbin/update-locale LANG=C.UTF-8  
# Install needed default locale for Makefly  
RUN echo 'en_US.UTF-8 UTF-8' >> /etc/locale.gen && \  
locale-gen  
# Set default locale for the environment  
ENV LC_ALL C.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US.UTF-8  
#CMD rake  
ENTRYPOINT cd /srv/ollert/ && /etc/init.d/mongod start && source
/usr/local/rvm/scripts/rvm && /bin/bash -l -c "rake"  

