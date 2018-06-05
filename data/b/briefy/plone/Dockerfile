FROM python:2.7-slim  
MAINTAINER Briefy <developers@briefy.co>  
  
RUN useradd --system -U -u 500 plone \  
&& mkdir -p /plone /data \  
&& chown -R plone:plone /plone /data  
  
ENV PLONE_MAJOR=5.0  
ENV PLONE_VERSION=5.0.8  
ENV PLONE_MD5=246788240851f48bc2f84289a3dc6480  
  
RUN buildDeps="curl sudo python-setuptools python-dev build-essential libssl-
dev libxml2-dev libxslt1-dev libbz2-dev libjpeg62-turbo-dev libmysqlclient-
dev" \  
&& runDeps="libmysqlclient-dev libxml2 libxslt1.1 libjpeg62 rsync" \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends $buildDeps \  
&& curl -o Plone.tgz -SL
https://launchpad.net/plone/$PLONE_MAJOR/$PLONE_VERSION/+download/Plone-$PLONE_VERSION-
UnifiedInstaller.tgz \  
&& echo "$PLONE_MD5 Plone.tgz" | md5sum -c - \  
&& tar -xzf Plone.tgz \  
&& ./Plone-$PLONE_VERSION-UnifiedInstaller/install.sh \  
\--password=admin \  
\--daemon-user=plone \  
\--owner=plone \  
\--group=plone \  
\--target=/plone \  
\--instance=instance \  
\--var=/data \  
none \  
&& cd /plone/instance \  
&& sed -i 's/eggs =/eggs =\n RelStorage\n MySQL-python\n plone.restapi/g'
buildout.cfg \  
&& sed -i 's/http-address = 8080/http-address = 8080\nrel-storage =\n keep-
history false\n blob-dir \/tmp\/blobcache\n shared-blob-dir false\n type
mysql\n compress true\n host HOST\n db DBNAME\n user USER\n passwd
PASS\n[versions]\nRelStorage=1.6.3\n/g' buildout.cfg \  
&& sudo -u plone bin/buildout \  
&& chown -R plone:plone /plone \  
&& rm -rf /Plone* \  
&& SUDO_FORCE_REMOVE=yes apt-get purge -y --auto-remove $buildDeps \  
&& apt-get install -y --no-install-recommends $runDeps \  
&& rm -rf /var/lib/apt/lists/* \  
&& rm -rf /plone/buildout-cache/downloads/* \  
&& find /plone \( -type f -a -name '*.pyc' -o -name '*.pyo' \) -exec rm -rf
'{}' +  
  
COPY docker-initialize.py docker-entrypoint.sh /  
  
EXPOSE 8080  
USER plone  
WORKDIR /plone/instance  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD ["start"]

