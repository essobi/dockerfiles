# RUBY  
FROM ruby:2.4.1  
MAINTAINER engineerhead@gmail.com  
  
# POSTGRES  
RUN echo "deb http://apt.postgresql.org/pub/repos/apt/ trusty-pgdg main 9.6" >
/etc/apt/sources.list.d/pgdg.list \  
&& wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-
key add \- \  
&& apt-get update && apt-get install -y \--no-install-recommends libpq-dev
postgresql-client-9.6  
  
# NODE  
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash - \  
&& apt-get install -y \--no-install-recommends nodejs  
  
# PhantomJS  
RUN apt-get install -y \--no-install-recommends libfontconfig \  
&& curl -sL
https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2
| tar -xj \  
&& ln -s $(pwd)/phantomjs-2.1.1-linux-x86_64/bin/phantomjs /bin/phantomjs  
  
RUN apt-get install -y \--no-install-recommends sudo software-properties-
common \  
&& add-apt-repository "deb https://cli-assets.heroku.com/branches/stable/apt
./" \  
&& curl -L https://cli-assets.heroku.com/apt/release.key | apt-key add \- \  
&& apt-get update \  
&& apt-get install heroku \  
&& rm -rf /var/lib/apt/lists/*  

