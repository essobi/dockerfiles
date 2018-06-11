FROM ubuntu:xenial  
  
MAINTAINER Andrej Antas <andrej@antas.cz>  
  
RUN rm /bin/sh && ln -s /bin/bash /bin/sh  
  
# Set the locale  
RUN apt-get clean && apt-get update && apt-get install -y locales  
RUN locale-gen en_US.UTF-8  
RUN export LANGUAGE=en_US.UTF-8  
RUN export LANG=en_US.UTF-8  
RUN export LC_ALL=en_US.UTF-8  
RUN locale-gen en_US.UTF-8  
RUN dpkg-reconfigure locales  
  
ENV TZ=Europe/Prague  
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone  
  
RUN apt-get update  
  
## Default Packages  
RUN apt-get install -y build-essential  
RUN apt-get install -y wget links curl rsync bc git git-core apt-transport-
https libxml2 libxml2-dev libcurl4-openssl-dev openssl  
RUN apt-get install -y gawk libreadline6-dev libyaml-dev autoconf libgdbm-dev
libncurses5-dev automake libtool bison libffi-dev  
RUN apt-get install -y libpq-dev xvfb qt5-default imagemagick
libqt5webkit5-dev libldap2-dev libsasl2-dev wkhtmltopdf pdftk libmysqlclient-
dev zip libgmp-dev  
RUN apt-get install -y openssh-client  
  
RUN apt-get install -y chromium-chromedriver  
  
RUN apt-get install -y software-properties-common  
  
## Latest version of Postgres from their repos  
RUN add-apt-repository "deb http://apt.postgresql.org/pub/repos/apt/ xenial-
pgdg main"  
RUN wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc |
apt-key add -  
RUN apt-get update  
RUN apt-get -y install postgresql-client  
  
# Nodejs engine  
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash -  
RUN apt-get install -y nodejs  
  
# install yarn  
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -  
RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee
/etc/apt/sources.list.d/yarn.list  
RUN apt-get update  
RUN apt-get install yarn  
  
# Ruby 2.4  
RUN apt-get install --reinstall ca-certificates  
RUN add-apt-repository ppa:brightbox/ruby-ng  
RUN apt-get update  
RUN apt-get install -y ruby2.4 ruby2.4-dev  
  
# Chromedriver whole setup (TODO: get CHROME_DRIVER_VERSION from
chromedriver.storage.googleapis.com/LATEST_RELEASE)  
ENV CHROME_DRIVER_VERSION=2.36  
ENV SELENIUM_STANDALONE_VERSION=3.4.0  
# TODO: get SELENIUM_STANDALONE_VERSION like so: $(echo
"$SELENIUM_STANDALONE_VERSION" | cut -d"." -f-2)  
ENV SELENIUM_SUBDIR=3.4  
RUN wget -N https://dl.google.com/linux/direct/google-chrome-
stable_current_amd64.deb -P ~/  
RUN dpkg -i --force-depends ~/google-chrome-stable_current_amd64.deb  
RUN apt-get -f install -y  
RUN dpkg -i --force-depends ~/google-chrome-stable_current_amd64.deb  
  
RUN wget -N
http://chromedriver.storage.googleapis.com/$CHROME_DRIVER_VERSION/chromedriver_linux64.zip
-P ~/  
RUN unzip ~/chromedriver_linux64.zip -d ~/  
RUN rm ~/chromedriver_linux64.zip  
RUN mv -f ~/chromedriver /usr/local/bin/chromedriver  
RUN chmod 0755 /usr/local/bin/chromedriver  
  
RUN wget -N http://selenium-
release.storage.googleapis.com/$SELENIUM_SUBDIR/selenium-server-
standalone-$SELENIUM_STANDALONE_VERSION.jar -P ~/  
RUN mv -f ~/selenium-server-standalone-$SELENIUM_STANDALONE_VERSION.jar
/usr/local/bin/selenium-server-standalone.jar  
RUN chown root:root /usr/local/bin/selenium-server-standalone.jar  
RUN chmod 0755 /usr/local/bin/selenium-server-standalone.jar  
  
RUN apt-get install -y zsh  
RUN wget https://github.com/robbyrussell/oh-my-zsh/raw/master/tools/install.sh
-O - | zsh || true  
  
RUN apt-get autoremove -y  
  
RUN gem install bundler  
  
ENV TINI_VERSION v0.16.1  
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini
/tini  
RUN chmod +x /tini  
  
RUN rm /bin/sh && ln -s /bin/zsh /bin/sh  
  
CMD ["/bin/zsh"]  

