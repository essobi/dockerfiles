FROM heroku/heroku:16-build  
  
RUN mkdir -p /app/user  
WORKDIR /app/user  
  
# ----- specify version  
ARG ruby_version=2.4.1  
# ruby abi version (${major}.${minor}.0)  
# ref: https://www.ruby-lang.org/en/news/2013/12/21/ruby-version-policy-
changes-with-2-1-0/  
# ex:  
# ruby 2.4.1 -> abi 2.4.0  
ARG bundle_version=2.4.0  
ARG node_version=6.9.4  
# /----- specify version  
ENV GEM_PATH /app/heroku/ruby/bundle/ruby/${bundle_version}  
ENV GEM_HOME /app/heroku/ruby/bundle/ruby/${bundle_version}  
RUN mkdir -p /app/heroku/ruby/bundle/ruby/${bundle_version}  
  
# Install Ruby  
RUN mkdir -p /app/heroku/ruby/ruby-${ruby_version}  
RUN curl -s --retry 3 -L heroku-buildpack-
ruby.s3.amazonaws.com/heroku-16/ruby-${ruby_version}.tgz | tar xz -C
/app/heroku/ruby/ruby-${ruby_version}  
ENV PATH /app/heroku/ruby/ruby-${ruby_version}/bin:$PATH  
  
# Install Node  
RUN curl -s --retry 3 -L
https://nodejs.org/download/release/v${node_version}/node-v${node_version}-linux-x64.tar.gz
| tar xz -C /app/heroku/ruby/  
RUN mv /app/heroku/ruby/node-v${node_version}-linux-x64
/app/heroku/ruby/node-${node_version}  
ENV PATH /app/heroku/ruby/node-${node_version}/bin:$PATH  
  
# Install Bundler  
WORKDIR /app/user  
RUN gem install bundler --no-ri --no-rdoc  
ENV PATH
/app/user/bin:/app/heroku/ruby/bundle/ruby/${bundle_version}/bin:$PATH  
ENV BUNDLE_APP_CONFIG /app/heroku/ruby/.bundle/config  
  
# Add source for yarn  
RUN curl -sS http://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -  
RUN echo "deb http://dl.yarnpkg.com/debian/ stable main" | tee
/etc/apt/sources.list.d/yarn.list  
  
# Install chrome and yarn  
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-
key add - \  
&& echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >>
/etc/apt/sources.list.d/google-chrome.list \  
&& apt-get update -qqy \  
&& apt-get -qqy install yarn xvfb google-chrome-stable libsqlite3-dev \  
&& rm /etc/apt/sources.list.d/google-chrome.list \  
&& rm -rf /var/lib/apt/lists/*  
  

