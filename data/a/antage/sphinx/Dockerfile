FROM debian:stable  
  
RUN \  
apt-get -y -q update \  
&& DEBIAN_FRONTEND=noninteractive \  
apt-get -y -q --no-install-recommends install \  
curl \  
ca-certificates \  
gosu \  
libmariadbclient18 \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* \  
&& rm /var/log/dpkg.log \  
&& curl -#L
https://github.com/kelseyhightower/confd/releases/download/v0.15.0/confd-0.15.0-linux-
amd64 -o /usr/local/bin/confd \  
&& chmod 755 /usr/local/bin/confd \  
&& mkdir -p /etc/confd/conf.d \  
&& mkdir -p /etc/confd/templates \  
&& touch /etc/confd/confd.toml \  
&& ln -s libmariadbclient.so.18 /usr/lib/x86_64-linux-gnu/libmariadb.so  
  
EXPOSE 9312  
EXPOSE 9306  
  
ENV LANG=C  
  
RUN \  
mkdir /etc/sphinxsearch \  
&& chown root:nogroup /etc/sphinxsearch \  
&& chmod 750 /etc/sphinxsearch \  
&& mkdir -p /var/lib/sphinxsearch/data \  
&& chown root:root /var/lib/sphinxsearch \  
&& chmod 755 /var/lib/sphinxsearch \  
&& chown nobody:nogroup /var/lib/sphinxsearch/data \  
&& chmod 750 /var/lib/sphinxsearch/data \  
&& mkdir -p /var/run/sphinxsearch \  
&& chown nobody:root /var/run/sphinxsearch \  
&& chmod 750 /var/run/sphinxsearch \  
&& mkdir /var/log/sphinxsearch \  
&& chown nobody:root /var/log/sphinxsearch \  
&& chmod 750 /var/log/sphinxsearch  
  
COPY bin/searchd /usr/bin/searchd  
COPY bin/indexer /usr/bin/indexer  
RUN \  
chown root:root /usr/bin/searchd \  
&& chmod 755 /usr/bin/searchd \  
&& chown root:root /usr/bin/indexer \  
&& chmod 755 /usr/bin/indexer  
COPY confd/sphinx.toml /etc/confd/conf.d/  
COPY conf/_sphinx_searchd.conf /etc/sphinxsearch/  
COPY docker-entrypoint.sh /  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD ["sphinx"]  

