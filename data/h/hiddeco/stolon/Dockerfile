FROM postgres:9.4  
RUN groupadd -r stolon && useradd -r -g stolon stolon  
  
ENV STOLON_VERSION v0.7.0  
RUN set -x \  
&& apt-get update; \  
apt-get install -y --no-install-recommends ca-certificates wget; \  
rm -rf /var/lib/apt/lists/* \  
&& wget -O release.tar.gz \  
"https://github.com/sorintlab/stolon/releases/download/${STOLON_VERSION}/stolon-${STOLON_VERSION}-linux-
amd64.tar.gz" \  
&& wget -O release.tar.gz.sig \  
"https://github.com/sorintlab/stolon/releases/download/${STOLON_VERSION}/stolon-${STOLON_VERSION}-linux-
amd64.tar.gz.sig" \  
&& export GNUPGHOME="$(mktemp -d)"; \  
gpg --keyserver keyserver.ubuntu.com --recv-keys
FCCCD6F144408817550264AD2DCA73AB1C4F0069 || \  
gpg --keyserver pool.sks-keyservers.net --recv-keys
FCCCD6F144408817550264AD2DCA73AB1C4F0069 || \  
gpg --keyserver pgp.rediris.es --recv-keys
FCCCD6F144408817550264AD2DCA73AB1C4F0069; \  
gpg --batch --verify release.tar.gz.sig release.tar.gz \  
&& rm -rf "$GNUPGHOME" release.tar.gz.sig \  
&& tar xf release.tar.gz; \  
cp "stolon-${STOLON_VERSION}-linux-amd64/bin/stolon-keeper"
"stolon-${STOLON_VERSION}-linux-amd64/bin/stolonctl" /usr/local/bin/; \  
chmod +x /usr/local/bin/stolon-keeper /usr/local/bin/stolonctl; \  
rm -rf "stolon-${STOLON_VERSION}-linux-amd64" release.tar.gz \  
&& apt-get purge -y --auto-remove ca-certificates wget  
  
COPY docker-entrypoint.sh /  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  

