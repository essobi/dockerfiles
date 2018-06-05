FROM debian:wheezy  
  
RUN groupadd -r beansdb && useradd -r -g beansdb beansdb  
  
RUN apt-get update && apt-get install -y --no-install-recommends \  
ca-certificates \  
curl \  
dh-autoreconf \  
&& rm -rf /var/lib/apt/lists/*  
  
ENV BEANSDB_VERSION 0.7.1.4  
ENV BEANSDB_DOWNLOAD_URL
https://github.com/douban/beansdb/archive/v0.7.1.4.tar.gz  
ENV BEANSDB_SHA1 4077be81f8bb034f16fbcad2d3fa0c00e930c167  
  
RUN buildDeps='gcc dh-autoreconf' \  
&& mkdir -p /usr/src/beansdb \  
&& curl -sSL "$BEANSDB_DOWNLOAD_URL" -o beansdb.tar.gz \  
&& echo "$BEANSDB_SHA1 *beansdb.tar.gz" | sha1sum -c - \  
&& tar -xzf beansdb.tar.gz -C /usr/src/beansdb --strip-components=1 \  
&& rm beansdb.tar.gz \  
&& cd /usr/src/beansdb \  
&& ./autogen.sh \  
&& ./configure \  
&& make \  
&& make install \  
&& rm -r /usr/src/beansdb \  
&& apt-get purge -y --auto-remove $buildDeps  
  
  
RUN mkdir -p /var/lib/beansdb \  
/var/log/beansdb \  
/etc/beansdb  
ADD beansdb_log.conf /etc/beansdb/beansdb_log.conf  
RUN chown -R beansdb /var/lib/beansdb \  
/etc/beansdb \  
/var/log/beansdb  
  
VOLUME /var/lib/beansdb  
WORKDIR /var/lib/beansdb  
  
EXPOSE 7900  
CMD ["beansdb", "-u", "beansdb", "-H", "/var/lib/beansdb", "-L",
"/etc/beansdb/beansdb_log.conf"]  

