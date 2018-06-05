FROM ruby:2.1.5  
RUN apt-get update \  
&& apt-get install -y build-essential zlib1g zlib1g-dev \  
libxml2 libxml2-dev libxslt-dev locate \  
libreadline6-dev libcurl4-openssl-dev git \  
libssl-dev libyaml-dev openssl autoconf libtool \  
ncurses-dev bison curl wget libpq-dev \  
libapr1 libaprutil1 libsvn1 \  
libpcap-dev libsqlite3-dev  
&& rm -rf /var/lib/apt/lists/*  
  
WORKDIR /opt/  
  
RUN git clone https://github.com/rapid7/metasploit-framework.git \  
&& cd metasploit-framework \  
&& bundle install --without development test coverage  
  
WORKDIR /root/  
  
RUN msfupdate  
  
CMD ["msfconsole"]  

