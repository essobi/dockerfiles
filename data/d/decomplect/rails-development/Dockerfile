FROM ubuntu:14.04  
MAINTAINER Sahil Muthoo <sahil@decomplect.io>  
  
RUN apt-get update -y \  
&& apt-get install -y --no-install-recommends \  
curl \  
software-properties-common \  
libxslt-dev \  
libxml2-dev \  
build-essential \  
&& apt-add-repository ppa:brightbox/ruby-ng \  
&& curl -sL https://deb.nodesource.com/setup_6.x | bash - \  
&& curl -sL https://anonscm.debian.org/cgit/pkg-postgresql/postgresql-
common.git/plain/pgdg/apt.postgresql.org.sh | bash - \  
&& apt-get install -y --no-install-recommends \  
ruby2.3 \  
ruby2.3-dev \  
nodejs \  
libpq-dev \  
postgresql-client \  
&& gem install bundler \  
&& gem update \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN useradd -ms /bin/bash rails  
  
USER rails  
  
VOLUME /home/rails/app  
  
WORKDIR /home/rails/app  
  
CMD ["bash"]

