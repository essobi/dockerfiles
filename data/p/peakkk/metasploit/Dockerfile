FROM ruby:2.4  
  
ENV REFRESHED_AT "2017-07-26 00:00:00"  
ENV MSF_DIR /metasploit-framework/  
  
RUN set -ex \  
&& apt-get -qq update \  
&& apt-get -y install \  
autoconf \  
bison \  
build-essential \  
curl \  
git-core \  
libapr1 \  
libaprutil1 \  
libcurl4-openssl-dev \  
libgmp3-dev \  
libpcap-dev \  
libpq-dev \  
libreadline6-dev \  
libsqlite3-dev \  
libssl-dev \  
libsvn1 \  
libtool \  
libxml2 \  
libxml2-dev \  
libxslt-dev \  
libyaml-dev \  
locate \  
ncurses-dev \  
openssl \  
postgresql \  
postgresql-contrib \  
wget \  
xsel \  
zlib1g \  
zlib1g-dev \  
&& rm -rf /var/lib/apt/lists/* \  
&& mkdir "$MSF_DIR"  
  
WORKDIR $MSF_DIR  
VOLUME /root/.msf4  
VOLUME /root/.msf5  
ENV PATH $PATH:$MSF_DIR  
  
RUN set -ex \  
&& git clone --depth=1 https://github.com/rapid7/metasploit-framework.git
$MSF_DIR \  
&& cd $MSF_DIR \  
&& git remote add upstream https://github.com/rapid7/metasploit-framework.git
\  
&& git config --global user.name "msf" \  
&& git config --global user.email "msf@example.com" \  
&& bundle install  
  
EXPOSE 80 8080 443 4444  
  
CMD ["msfconsole"]  

