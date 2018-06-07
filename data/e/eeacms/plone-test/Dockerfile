FROM plone:4  
MAINTAINER "EEA: IDM2 A-Team" <eea-edw-a-team-alerts@googlegroups.com>  
  
USER root  
  
RUN runDeps="curl git gcc libc-dev ImageMagick ghostscript
libmagickcore-6.q16-2-extra graphviz libjpeg62-turbo-dev" \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends $runDeps \  
&& apt-get -o Dpkg::Options::="--force-confmiss" install --reinstall --no-
install-recommends netbase \  
&& rm -rf /var/lib/apt/lists/* \  
&& mv develop.cfg develop-plone.cfg \  
&& mv /docker-entrypoint.sh /plone-entrypoint.sh  
  
USER plone  
COPY develop.cfg /plone/instance/  
RUN /plone/Python-2.7/bin/pip install pip==9.0.3 \  
&& /plone/Python-2.7/bin/python bootstrap.py -c develop.cfg  
RUN bin/buildout -c develop.cfg  
COPY docker-entrypoint.sh /  

