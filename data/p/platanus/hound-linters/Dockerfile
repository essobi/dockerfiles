FROM ruby:2.4.1  
RUN apt-get update && apt-get install -y apt-transport-https \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Add node source  
RUN curl -s https://deb.nodesource.com/gpgkey/nodesource.gpg.key | apt-key add
-  
RUN echo 'deb https://deb.nodesource.com/node_8.x jessie main' >
/etc/apt/sources.list.d/nodesource.list  
RUN echo 'deb-src https://deb.nodesource.com/node_8.x jessie main' >>
/etc/apt/sources.list.d/nodesource.list  
  
# Add yarn source  
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -  
RUN echo 'deb https://dl.yarnpkg.com/debian/ stable main' >
/etc/apt/sources.list.d/yarn.list  
  
RUN apt-get update && apt-get install -y --no-install-recommends \  
locales \  
nodejs \  
yarn \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias
en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US.UTF-8  
ENV LC_ALL en_US.UTF-8  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
COPY Gemfile /usr/src/app/  
COPY Gemfile.lock /usr/src/app/  
RUN bundle install  
  
COPY package.json /usr/src/app/  
COPY yarn.lock /usr/src/app/  
RUN yarn  
  
COPY . /usr/src/app  
  
CMD bundle exec rake jobs:work  

