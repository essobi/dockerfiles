# Pelican ready-to-go.  
FROM justifiably/python3  
  
# Version change should trigger a rebuild  
ENV PELICAN_VERSION=3.7.0  
# Install commonly used requirements  
RUN apk --update --no-cache add libpng bash curl yaml gettext su-exec inotify-
tools && \  
apk --no-cache add --virtual build-dependencies python3-dev yaml-dev build-
base \  
&& pip3 install -U pip pelican==$PELICAN_VERSION Markdown pyyaml pygments
feedparser feedgenerator typogrify awesome-slugify beautifulsoup4 \  
&& apk del build-dependencies python3-dev yaml-dev build-base \  
&& rm -r /root/.cache  
  
RUN adduser -G users -S -u 1001 pelican && \  
mkdir -p /srv/pelican/{output,content,config} && \  
chown -R pelican.users /srv/  
  
VOLUME ['/srv/pelican/config','/srv/pelican/content','/srv/pelican/output']  
ADD runpelican.sh /srv/pelican/config/  
ADD pelicanconf.py /srv/pelican/config/  
  
WORKDIR /srv/pelican/config  
CMD ["su-exec", "pelican:users", "/srv/pelican/config/runpelican.sh"]  

