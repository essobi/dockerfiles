FROM ubuntu:13.10  
RUN apt-get update && apt-get install -y build-essential git wget curl
libcurl3 libcurl3-gnutls libcurl4-openssl-dev libffi-dev \  
libffi6 libgdbm-dev libgvc5 libmagickwand-dev imagemagick libncurses5
libncurses5-dev libncurses5-dbg libc6-dev \  
libsasl2-dev libxslt-dev libossp-uuid-dev libpq-dev libreadline6
libreadline6-dev libssl-dev libyaml-0-2 libyaml-dev \  
libtool libxml2-dev zlib1g zlib1g-dev software-properties-common python-
software-properties socat mysql-client libmysqlclient-dev postgresql-client  
  
ADD configs /opt/configs  
ADD scripts /opt/scripts  
  
RUN sh /opt/scripts/nodejs/install.sh 0.10.29  
  
RUN sh /opt/scripts/ruby-install/install.sh 0.4.3  
RUN sh /opt/scripts/ruby/install.sh  
  
RUN sh /opt/scripts/lein/install.sh  

