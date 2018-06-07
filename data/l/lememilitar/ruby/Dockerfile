FROM heroku/cedar:14  
MAINTAINER George Moura <george@lememilitar.com>  
  
RUN mkdir -p /app/user  
WORKDIR /app/user  
  
ENV RUBY_VERSION ruby-2.2.3  
ENV FREETDS_VERSION freetds-0.91.112  
ENV TDSVER 7.0  
ENV GEM_PATH /app/heroku/ruby/bundle/ruby/2.2.0  
ENV GEM_HOME /app/heroku/ruby/bundle/ruby/2.2.0  
RUN mkdir -p /app/heroku/ruby/bundle/ruby/2.2.0  
  
# Install Ruby  
RUN mkdir -p /app/heroku/ruby/$RUBY_VERSION  
RUN curl -s --retry 3 -L https://heroku-buildpack-
ruby.s3.amazonaws.com/cedar-14/$RUBY_VERSION.tgz | tar xz -C
/app/heroku/ruby/$RUBY_VERSION  
ENV PATH /app/heroku/ruby/$RUBY_VERSION/bin:$PATH  
  
# Install Node  
RUN curl -s --retry 3 -L
http://s3pository.heroku.com/node/v0.12.7/node-v0.12.7-linux-x64.tar.gz | tar
xz -C /app/heroku/ruby/  
RUN mv /app/heroku/ruby/node-v0.12.7-linux-x64 /app/heroku/ruby/node-0.12.7  
ENV PATH /app/heroku/ruby/node-0.12.7/bin:$PATH  
  
# Install Bundler  
RUN gem install bundler -v 1.9.10 --no-ri --no-rdoc  
ENV PATH /app/user/bin:/app/heroku/ruby/bundle/ruby/2.2.0/bin:$PATH  
ENV BUNDLE_APP_CONFIG /app/heroku/ruby/.bundle/config  
  
# Run bundler to cache dependencies  
ONBUILD COPY ["Gemfile", "Gemfile.lock", "/app/user/"]  
ONBUILD RUN bundle install --path /app/heroku/ruby/bundle --jobs 4  
ONBUILD ADD . /app/user  
  
# How to conditionally `rake assets:precompile`?  
ONBUILD ENV RAILS_ENV production  
ONBUILD ENV SECRET_KEY_BASE $(openssl rand -base64 32)  
ONBUILD RUN if [ -f /app/user/Rakefile ]; then bundle exec rake
assets:precompile; fi  
  
# export env vars during run time  
RUN mkdir -p /app/.profile.d/  
RUN echo "cd /app/user/" > /app/.profile.d/home.sh  
ONBUILD RUN echo "export PATH=\"$PATH\" GEM_PATH=\"$GEM_PATH\"
GEM_HOME=\"$GEM_HOME\" RAILS_ENV=\"\${RAILS_ENV:-$RAILS_ENV}\"
SECRET_KEY_BASE=\"\${SECRET_KEY_BASE:-$SECRET_KEY_BASE}\"
BUNDLE_APP_CONFIG=\"$BUNDLE_APP_CONFIG\"" > /app/.profile.d/ruby.sh  
  
# Intalll TDS  
RUN curl -s ftp://ftp.freetds.org/pub/freetds/stable/$FREETDS_VERSION.tar.gz |
tar xvz -C /tmp  
WORKDIR /tmp/$FREETDS_VERSION  
RUN ./configure --disable-shared --disable-installed --with-tdsver=$TDSVER
\--enable-msdblib --with-gnu-ld  
RUN make DESTDIR=/app install  
RUN touch /app/usr/local/include/tds.h  
RUN touch /app/usr/local/lib/libtds.a  
RUN echo "export PATH=\"/app/usr/local/bin:\$PATH\"" >>
/app/.profile.d/freetds.sh  
  
WORKDIR /app/user  
  
COPY ./init.sh /usr/bin/init.sh  
RUN chmod +x /usr/bin/init.sh  
  
ENTRYPOINT ["/usr/bin/init.sh"]  

