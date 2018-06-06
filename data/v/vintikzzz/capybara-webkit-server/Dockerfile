FROM buildpack-deps:xenial  
  
# skip installing gem documentation  
RUN mkdir -p /usr/local/etc \  
&& { \  
echo 'install: --no-document'; \  
echo 'update: --no-document'; \  
} >> /usr/local/etc/gemrc  
  
ENV BUNDLER_VERSION 1.11.2  
# some of ruby's build scripts are written in ruby  
# we purge this later to make sure our final image uses what we just built  
RUN set -ex \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends ruby-dev qt4-default libqt4-dev
libqtwebkit-dev gstreamer1.0-plugins-base gstreamer1.0-tools gstreamer1.0-x
xvfb dbus-x11 monit gettext-base \  
&& gem install bundler --version "$BUNDLER_VERSION" \  
&& rm -rf /var/lib/apt/lists/*  
  
# install things globally, for great justice  
# and don't create ".bundle" in all our apps  
ENV GEM_HOME /bundle  
ENV BUNDLE_PATH="$GEM_HOME" \  
BUNDLE_BIN="$GEM_HOME/bin" \  
BUNDLE_SILENCE_ROOT_WARNING=1 \  
BUNDLE_APP_CONFIG="$GEM_HOME" \  
WEBKIT_PORT=40000 \  
WEBKIT_LOG=/var/log/webkit_server.log \  
RACK_ENV=production \  
APP_DIR=/usr/src/app \  
PIDFILE=/var/run/webkit_server.pid \  
XVFB_RES=1024x768x16 \  
DISPLAY=:99 \  
MONIT_LOG=/var/log/monit.log \  
XVFB_PIDFILE=/var/run/xvfb.pid  
ENV PATH $BUNDLE_BIN:$PATH  
RUN mkdir -p "$GEM_HOME" "$BUNDLE_BIN" \  
&& mkdir -p "$APP_DIR" \  
&& git init  
  
WORKDIR $APP_DIR  
  
# throw errors if Gemfile has been modified since Gemfile.lock  
RUN bundle config --global frozen 1  
  
COPY Gemfile* capybara-webkit.gemspec $APP_DIR/  
COPY lib/capybara/webkit/version.rb $APP_DIR/lib/capybara/webkit/  
  
RUN bundle install --without development test  
  
COPY . $APP_DIR  
  
RUN bundle exec rake build  
  
RUN rm -rf src \  
&& rm -rf test \  
&& chmod +x server.sh \  
&& chmod +x run.sh \  
&& chmod +x xvfb.sh  
  
EXPOSE $WEBKIT_PORT  
  
CMD ["/bin/sh", "./run.sh"]  

