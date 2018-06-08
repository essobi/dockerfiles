FROM ubuntu:16.04  
#Credit goes to Lloyd Watkin for creation of entrypoint.sh & dependencies.  
MAINTAINER Ph30nix <ph30nix@protonmail.com  
  
# Install dependencies  
RUN apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \  
lsb-base \  
adduser \  
libidn11 \  
libssl1.0.0 \  
lua-bitop \  
lua-dbi-mysql \  
lua-dbi-postgresql \  
lua-dbi-sqlite3 \  
lua-event \  
luarocks \  
libexpat-dev \  
lua-filesystem \  
lua-sec \  
lua-socket \  
lua-zlib \  
lua5.1 \  
openssl \  
ca-certificates \  
ssl-cert \  
unzip \  
gcc \  
git \  
make \  
build-essential \  
libidn11-dev \  
libssl-dev \  
&& rm -rf /var/lib/apt/lists/* \  
&& luarocks install luaexpat  
  
#Add user for Prosody to run as.  
RUN useradd -m -c "Prosody user" prosody -s /bin/bash  
  
#Create and set permissions for log directory.  
RUN mkdir /var/log/prosody && chown -R prosody: /var/log/prosody  
  
#Make prosody owner of the program directory.  
RUN mkdir -p /usr/local/var/lib/prosody  
RUN chown -R prosody: /usr/local/var/lib/prosody  
  
#Download latest source and compile & install.  
WORKDIR /tmp  
RUN git clone https://github.com/bjc/prosody.git && cd prosody;  
RUN cd /tmp/prosody && ./configure --ostype=debian --sysconfdir=/etc/prosody
&& make && make install  
  
#Set permissions on the application scripts.  
RUN chown -R prosody: /usr/local/bin/  
  
#Make make set permissions for PID file.  
RUN mkdir /var/run/prosody && chown -R prosody: /var/run/prosody  
  
#Add entrypoint and set file permissions.  
COPY ./entrypoint.sh /entrypoint.sh  
RUN chmod 755 /entrypoint.sh  
RUN chmod -R 770 /usr/local/bin  
WORKDIR /usr/local/bin  
ENTRYPOINT ["/entrypoint.sh"]  
EXPOSE 80 443 5222 5269 5347 5280 5281  
USER prosody  
ENV __FLUSH_LOG yes  
CMD ["prosody"]  

