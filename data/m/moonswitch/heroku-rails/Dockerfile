FROM heroku/heroku:16-build  
MAINTAINER Jeff French <jeff.french@moonswitch.com>  
  
# Which versions?  
ENV RUBY_VERSION=2.5.1 \  
BUNDLER_VERSION=1.15.2 \  
NODE_VERSION=8.10.0 \  
YARN_VERSION=1.0.2  
  
# Setup the environment  
ENV LC_ALL=en_US.UTF-8 \  
GEM_PATH=/app/heroku/ruby/bundle/ruby/$RUBY_VERSION \  
GEM_HOME=/app/heroku/ruby/bundle/ruby/$RUBY_VERSION \  
PATH=/app/heroku/ruby/ruby-$RUBY_VERSION/bin:/app/heroku/ruby/node-$NODE_VERSION/bin:/app/heroku/ruby/yarn-$YARN_VERSION/bin:/app/user/bin:/app/heroku/ruby/bundle/ruby/$RUBY_VERSION/bin:$PATH
\  
BUNDLE_APP_CONFIG=/app/heroku/ruby/.bundle/config \  
WORKDIR_PATH=/app/user \  
SCRIPT_PATH=/app/profile.d  
  
# Add the init script  
COPY ./init.sh /usr/bin/init.sh  
  
# Install all the tooling  
RUN set -e ;\  
echo "Setting up directories and installing Ruby v${RUBY_VERSION}, Node
v${NODE_VERSION}, Yarn v${YARN_VERSION}, and Bundler v${BUNDLER_VERSION}..."
;\  
#####  
# Setup directories  
#  
mkdir -p "${WORKDIR_PATH}" ;\  
mkdir -p "${SCRIPT_PATH}" ;\  
mkdir -p /app/heroku/ruby/bundle/ruby/$RUBY_VERSION ;\  
#####  
# Make the init script executable  
#####  
chmod +x /usr/bin/init.sh ;\  
#####  
# Install Ruby  
#####  
mkdir -p /app/heroku/ruby/ruby-$RUBY_VERSION ;\  
curl -s --retry 3 -L https://heroku-buildpack-
ruby.s3.amazonaws.com/heroku-16/ruby-$RUBY_VERSION.tgz | tar xz -C
/app/heroku/ruby/ruby-$RUBY_VERSION ;\  
#####  
# Install Node  
#####  
curl -s --retry 3 -L
http://s3pository.heroku.com/node/v$NODE_VERSION/node-v$NODE_VERSION-
linux-x64.tar.gz | tar xz -C /app/heroku/ruby/ ;\  
mv /app/heroku/ruby/node-v$NODE_VERSION-linux-x64
/app/heroku/ruby/node-$NODE_VERSION ;\  
#####  
# Install Yarn  
#####  
curl -s --retry 3 -L
https://yarnpkg.com/downloads/$YARN_VERSION/yarn-v$YARN_VERSION.tar.gz | tar
xz -C /app/heroku/ruby/ ;\  
mv /app/heroku/ruby/yarn-v$YARN_VERSION /app/heroku/ruby/yarn-$YARN_VERSION ;\  
#####  
# Install Bundler  
#####  
gem install bundler -v $BUNDLER_VERSION --no-ri --no-rdoc ;\  
#####  
# export env vars during run time  
#####  
echo "cd /app/user/" > "${SCRIPT_PATH}/home.sh" ;\  
echo "export PATH=\"$PATH\" GEM_PATH=\"$GEM_PATH\" GEM_HOME=\"$GEM_HOME\"
SECRET_KEY_BASE=\"$SECRET_KEY_BASE\" BUNDLE_APP_CONFIG=\"$BUNDLE_APP_CONFIG\""
> "${SCRIPT_PATH}/ruby.sh"  
  
WORKDIR /app/user  
  
# Run bundler to cache dependencies  
ONBUILD COPY ["Gemfile", "Gemfile.lock", "${WORKDIR_PATH}/"]  
ONBUILD RUN bundle install --path /app/heroku/ruby/bundle --jobs 4  
  
# run npm or yarn install  
# add yarn.lock to .slugignore in your project  
ONBUILD COPY package*.json yarn.* "${WORKDIR_PATH}/"  
ONBUILD RUN [ -f yarn.lock ] && yarn install --no-progress || npm install  
  
# Add all files  
ONBUILD ADD . "${WORKDIR_PATH}"  
  
ENTRYPOINT ["/usr/bin/init.sh"]

