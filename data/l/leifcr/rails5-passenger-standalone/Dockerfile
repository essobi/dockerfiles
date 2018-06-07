FROM ruby:2.4  
  
LABEL maintainer leifcr@gmail.com  
# Location of the STI scripts inside the image.  
LABEL io.openshift.s2i.scripts-url=image:///usr/local/bin/s2i \  
# DEPRECATED: This label will be kept here for backward compatibility.  
io.s2i.scripts-url=image:///usr/local/bin/s2i \  
summary="Platform for building and running Rails 5 with Ruby 2.4 including
extra packages" \  
io.k8s.description="Platform for building and running Rails 5 with Ruby 2.4
including extra packages" \  
io.k8s.display-name="Ruby 2.4 (Rails 5)" \  
io.openshift.expose-services="8080:http" \  
io.openshift.tags="builder,ruby,ruby24,rails5,rails"  
  
EXPOSE 8080  
  
# The $HOME is not set by default, but some applications needs this variable  
ENV APP_HOME=/app \  
HOME=/app \  
STI_SCRIPTS_PATH=/usr/local/bin/s2i \  
RUBY_VERSION=2.4 \  
LANG=C.UTF-8 \  
RAILS_ENV=production \  
APP_USER=rails \  
APP_USER_UID=1010  
  
# ENV PATH=/app/bin:$PATH  
  
# Add https transport to apt  
# RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-
selections \  
# && apt-get update -qq && apt-get install -y apt-transport-https apt-utils
ca-certificates  
  
# For staging and production env, duck-cli must be installed to be able to
download refile assets  
  
# # Install nss-wrapper from unstable.  
# COPY apt/unstable.pref /etc/apt/preferences.d/unstable.pref  
# COPY apt/unstable.list /etc/apt/sources.list.d/unstable.list  
# && apt-get install -y -t unstable libnss-wrapper \  
  
# Install updated nodejs, yarn and build packages  
# RUN curl -sL https://deb.nodesource.com/setup_7.x | bash - \  
RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-
selections \  
&& apt-get update -qq && apt-get install -y apt-transport-https apt-utils ca-
certificates \  
&& curl -s https://deb.nodesource.com/gpgkey/nodesource.gpg.key | apt-key add
- \  
&& echo "deb https://deb.nodesource.com/node_8.x jessie main" >
/etc/apt/sources.list.d/nodesource.list \  
&& echo "deb-src https://deb.nodesource.com/node_8.x jessie main" >>
/etc/apt/sources.list.d/nodesource.list \  
&& curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - \  
&& echo "deb http://dl.yarnpkg.com/debian/ stable main" | tee
/etc/apt/sources.list.d/yarn.list \  
&& apt-get update -qq \  
&& apt-get install -y build-essential libxslt1-dev libxml2-dev libmysqlclient-
dev mysql-client libpq-dev postgresql-client wget nodejs tar unzip rsync lsb-
release yarn nano vim cmake \  
# && apt-get install -y duck \  
&& git clone git://git.samba.org/nss_wrapper.git /tmp/nss_wrapper \  
&& cd /tmp/nss_wrapper \  
&& git checkout nss_wrapper-1.1.3 \  
&& mkdir /tmp/nss_wrapper/build \  
&& cd /tmp/nss_wrapper/build \  
&& cmake -DCMAKE_INSTALL_PREFIX=/usr/local -DLIB_SUFFIX=64 .. \  
&& make \  
&& make install \  
&& rm -rf /tmp/nss_wrapper \  
&& groupadd -g $APP_USER_UID $APP_USER \  
&& useradd --uid $APP_USER_UID -s /bin/bash -m -d $APP_HOME -g $APP_USER_UID
-G root $APP_USER \  
&& chown $APP_USER_UID:0 $APP_HOME \  
&& chmod 775 $APP_HOME \  
&& chmod g+s $APP_HOME \  
&& mkdir -p $APP_HOME/.ssh/ \  
&& chmod 700 $APP_HOME/.ssh \  
&& touch $APP_HOME/.ssh/known_hosts \  
&& ssh-keyscan bitbucket.org >> $APP_HOME/.ssh/known_hosts \  
&& ssh-keyscan github.com >> $APP_HOME/.ssh/known_hosts \  
&& chown -R $APP_USER_UID:0 /usr/local/bundle \  
&& chmod 775 /usr/local/bundle \  
&& chmod g+s /usr/local/bundle \  
&& apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# # build nss_wrapper  
# RUN git clone git://git.samba.org/nss_wrapper.git /tmp/nss_wrapper && \  
# cd /tmp/nss_wrapper && \  
# git checkout nss_wrapper-1.1.3 && \  
# mkdir /tmp/nss_wrapper/build && \  
# cd /tmp/nss_wrapper/build && \  
# cmake -DCMAKE_INSTALL_PREFIX=/usr/local -DLIB_SUFFIX=64 .. && \  
# make && \  
# make install && \  
# rm -rf /tmp/nss_wrapper  
  
# For passenger:  
# && apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys
561F9B9CAC40B2F7 \  
# && echo "deb https://oss-binaries.phusionpassenger.com/apt/passenger jessie
main" > /etc/apt/sources.list.d/passenger.list \  
# passenger  
  
# Cannot install duck, as it requires root on install  
# See: https://trac.cyberduck.io/browser/trunk/setup/deb/duck.postinstall
(need to submit ticket)  
# RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys
FE7097963FEFBE72 \  
# && echo "deb https://s3.amazonaws.com/repo.deb.cyberduck.io stable main" |
tee /etc/apt/sources.list.d/duck.list \  
# && apt-get update -qq && apt-get install -y duck  
  
# RUN apt-get install -y libxslt1-dev  
# RUN apt-get install -y libxml2-dev  
# RUN apt-get install -y libmysqlclient-dev  
# RUN apt-get install -y mysql-client  
# RUN apt-get install -y libpq-dev  
# RUN apt-get install -y postgresql-client  
# RUN apt-get install -y wget  
# RUN apt-get install -y nodejs  
# RUN apt-get install -y tar  
# RUN apt-get install -y unzip  
# RUN apt-get install -y duck  
# RUN apt-get install -y lsb-release  
# RUN apt-get install -y yarn  
  
# libmariadbd-dev \  
  
# Create application folder  
# Setup rails user group and rails user  
# Set rails:rails as user on app folder  
# RUN groupadd -g $APP_USER_UID $APP_USER && \  
# useradd --uid $APP_USER_UID -s /bin/bash -m -d $APP_HOME -g $APP_USER_UID -G
root $APP_USER && \  
# chown $APP_USER_UID:0 $APP_HOME && \  
# chmod 775 $APP_HOME && \  
# chmod g+s $APP_HOME && \  
# mkdir -p $APP_HOME/.ssh/ && \  
# chmod 700 $APP_HOME/.ssh && \  
# touch $APP_HOME/.ssh/known_hosts && \  
# ssh-keyscan bitbucket.org >> $APP_HOME/.ssh/known_hosts && \  
# ssh-keyscan github.com >> $APP_HOME/.ssh/known_hosts && \  
# chown -R $APP_USER_UID:0 /usr/local/bundle && \  
# chmod 775 /usr/local/bundle && \  
# chmod g+s /usr/local/bundle  
  
# Copy contrib  
COPY ./contrib/ $APP_HOME  
  
# Copy bin  
COPY bin/ /usr/local/bin/  
COPY s2i/bin $STI_SCRIPTS_PATH  
  
# Set workdir to /app, so COPY, ADD, RUN and ENTRYPOINT is run within folder  
WORKDIR $APP_HOME  
  
# Copy app  
# COPY . ./  
# Install gems (Base gems used for most apps to save deployment time)  
# Add yarn and gemfiles  
# COPY Gemfile Gemfile.lock package.json yarn.lock ./  
# Add yarn files  
# COPY package.json yarn.lock ./  
# Add Gemfile  
COPY Gemfile Gemfile.lock ./  
  
RUN chown -R $APP_USER_UID:0 $APP_HOME \  
&& chown -R $APP_USER_UID:0 /usr/local/bundle \  
&& /usr/local/bin/fix-permissions /usr/local/bundle \  
&& /usr/local/bin/fix-permissions $APP_HOME \  
&& chmod 700 $APP_HOME/.ssh \  
&& rm -rf /tmp/* /var/tmp/*  
  
# Continue as rails user  
USER 1010  
  
# Install gems and yarn/node_modules  
# RUN gem install bundler && \  
# bundle install --deployment --jobs 20 --retry 5 && \  
# yarn install  
  
# Install only gems  
RUN gem install bundler \  
&& bundle install --deployment --jobs 20 --retry 5  
  
ENTRYPOINT ["container-entrypoint"]  
# CMD ["usage"]  
CMD ["$STI_SCRIPTS_PATH/usage"]  
  
# Set entry point to bundle exec, as all cmd's with rails should be prepended  
# ENTRYPOINT ["start.sh"]  
# CMD ["rails", "server"]  

