FROM ubuntu:14.04  
MAINTAINER Carlos José Vaz <carlosjvaz@gmail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
# update repositories  
RUN apt-get -y update  
  
# install system deps  
RUN apt-get -y -qq install \  
linux-headers-generic \  
python-software-properties \  
software-properties-common  
  
# install utils programs  
RUN apt-get -y -qq install build-essential \  
make \  
cmake \  
vim \  
git \  
sudo \  
zip \  
bzip2 \  
fontconfig \  
curl \  
vim \  
python-dev \  
ruby-dev  
  
# prepare locales  
RUN echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen  
RUN echo "pt_BR.UTF-8 UTF-8" >> /etc/locale.gen  
RUN locale-gen --purge --lang en_US \  
&& locale-gen --purge --lang pt_BR \  
&& locale-gen  
  
##### PYTHON ####  
# install virtualenv  
RUN apt-get -y -qq install python-setuptools  
RUN easy_install pip  
RUN pip install virtualenv virtualenvwrapper  
  
##### PHP #####  
# install PHP without apache  
RUN apt-get -y -qq install php5-cli php5-gd php5-mysql \  
php5-pgsql php5-ldap php5-imap \  
php5-sqlite php5-mcrypt php5-curl \  
php-pear php5-memcache php5-ps \  
php5-xmlrpc php5-xsl  
  
# install composer  
RUN curl -sS https://getcomposer.org/installer | php  
RUN mv composer.phar /usr/local/bin/composer  
  
#### JAVA #####  
# install java8  
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle  
RUN add-apt-repository ppa:webupd8team/java -y  
RUN apt-get -y update  
RUN echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select
true | /usr/bin/debconf-set-selections  
RUN apt-get -y install oracle-java8-installer && apt-get clean  
RUN update-java-alternatives -s java-8-oracle  
  
# install maven  
ENV MAVEN_VERSION 3.3.1  
ENV M2_HOME /opt/maven  
ENV M2 /opt/maven/bin  
ENV PATH $M2:$PATH  
RUN cd /tmp && \  
wget
http://ftp.unicamp.br/pub/apache/maven/maven-3/$MAVEN_VERSION/binaries/apache-
maven-$MAVEN_VERSION-bin.tar.gz \  
&& tar zxvf apache-maven-$MAVEN_VERSION-bin.tar.gz \  
&& mv apache-maven-$MAVEN_VERSION /opt/maven \  
&& rm apache-maven-$MAVEN_VERSION-bin.tar.gz \  
&& ln -s /opt/maven/bin/mvn /usr/bin/mvn  
  
##### NODE ######  
# install Node.js v0.12 and NPM  
RUN curl -sL https://deb.nodesource.com/setup_0.12 | bash -  
RUN apt-get install -y nodejs  
RUN npm install -g npm  
  
# install yeoman, bower, grunt e gulp  
RUN npm install -g yo  
RUN npm install -g bower  
RUN npm install -g grunt-cli  
RUN npm install -g gulp  
  
# install yeoman generators  
RUN npm install -g generator-angular  
RUN npm install -g generator-gulp-angular  
RUN npm install -g generator-gulp-webapp  
RUN npm install -g generator-jhipster@2.16.1  
RUN npm install -g generator-angular-flask  
RUN npm install -g ionic  
RUN npm install -g cordova  
  
##### RUBY ######  
# install rbenv and ruby-build  
RUN apt-get install -y zlib1g-dev libssl-dev libreadline-dev libyaml-dev \  
libsqlite3-dev sqlite3 libxml2-dev libxslt1-dev \  
libcurl4-openssl-dev python-software-properties libffi-dev  
  
RUN git clone https://github.com/sstephenson/rbenv.git /root/.rbenv  
RUN git clone https://github.com/sstephenson/ruby-build.git
/root/.rbenv/plugins/ruby-build  
RUN /root/.rbenv/plugins/ruby-build/install.sh  
ENV PATH /root/.rbenv/bin:$PATH  
RUN echo 'eval "$(rbenv init -)"' >> /etc/profile.d/rbenv.sh # or /etc/profile  
RUN echo 'eval "$(rbenv init -)"' >> .bashrc  
RUN echo 'gem: --no-rdoc --no-ri' >> /.gemrc  
  
# Install Ruby  
RUN rbenv install 2.2.2  
RUN rbenv global 2.2.2  
RUN rbenv rehash  
  
# Install Bundler  
RUN gem install --no-ri --no-rdoc bundler  
  
# RAILS  
RUN gem install rails -v 4.2.2  
  
# sass and compass  
RUN gem install sass compass  
  
#### CLIENTS DB #####  
RUN apt-get install -y mysql-client postgresql-client sqlite3 --no-install-
recommends && rm -rf /var/lib/apt/lists/*  
  
##### HEROKU TOLLBELT ######  
RUN wget -qO- https://toolbelt.heroku.com/install-ubuntu.sh | sh  
  
##### USER ######  
# create user developer  
RUN echo 'root:developer' |chpasswd  
RUN groupadd developer && useradd developer -s /bin/bash -m -g developer -G
developer && adduser developer sudo  
RUN echo 'developer:developer' |chpasswd  
RUN mkdir /home/developer/projects && chown developer:developer
/home/developer/projects  
  
# Define working directory.  
VOLUME ["/home/developer/projects"]  
WORKDIR /home/developer  
  
# expose the working directory, the Tomcat port, the Grunt server port, the
SSHD port and run SSHD  
EXPOSE 8080 3000 3001  
CMD ["/bin/bash"]

