FROM debian:stretch  
LABEL maintainer="s7b4 <baron.stephane@gmail.com>"  
  
ENV APP_USER=lstu \  
APP_TAG=0.17-1 \  
GOSU_VERSION=1.10  
ENV APP_HOME=/opt/$APP_USER \  
APP_WORK=/home/$APP_USER  
  
# set user/group IDs  
RUN groupadd -r "$APP_USER" \--gid=999 \  
&& useradd -m -r -g "$APP_USER" \--uid=999 "$APP_USER"  
  
# Perl base  
RUN apt-get update --quiet \  
&& apt-get install --no-install-recommends --quiet --yes \  
procps \  
make \  
curl \  
sqlite3 \  
ca-certificates \  
gcc \  
libperl-dev \  
libpq-dev \  
libsqlite3-dev \  
libssl-dev \  
zlib1g-dev \  
libpng-dev \  
default-libmysqlclient-dev \  
carton \  
libmodule-install-perl \  
&& apt-get clean --quiet \  
&& rm -rf /var/lib/apt/lists/*  
  
# Gosu  
RUN curl -o /usr/local/sbin/gosu -sSL
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$(dpkg
--print-architecture | awk -F- '{ print $NF }')" \  
&& chmod +x /usr/local/sbin/gosu  
  
# Install lstu  
RUN mkdir -p $APP_HOME $APP_WORK \  
&& curl -sSL
"https://framagit.org/luc/lstu/repository/archive.tar.gz?ref=$APP_TAG" \  
| tar xz --strip-component=1 -C $APP_HOME \  
&& cd $APP_HOME \  
&& make installdeps \  
&& rm -rf "$APP_HOME/log" "$APP_HOME/t" \  
&& rm -rf "$HOME/.cpan"*  
  
COPY scripts/entrypoint.sh /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  
  
EXPOSE 8080  
VOLUME $APP_WORK  

