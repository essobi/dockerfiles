FROM lochnair/base:alpine-python27  
MAINTAINER Lochnair <me@lochnair.net>  
  
LABEL Description="Docker image for pyLoad"  
  
## Environment variables  
ENV PGID 2000  
ENV PUID 2000  
## Expose ports  
EXPOSE 8001  
## Create pyload user  
RUN addgroup pyload  
RUN adduser -G pyload -D pyload  
  
## Install packages  
RUN apk add \  
\--no-cache \  
\--update \  
git \  
py2-curl \  
py-feedparser \  
py-imaging \  
py2-jinja2 \  
py2-openssl \  
py2-simplejson \  
shadow  
  
# Install additional Python modules  
RUN pip install beaker; \  
pip install thrift  
  
# Clone pyload from GitHub  
RUN git clone https://github.com/pyload/pyload.git /app  
  
# Remove build tools  
RUN apk del \  
build-base \  
git \  
python2-dev  
  
COPY pyload.conf /config/pyload.conf  
RUN touch /config/setup.lock  
  
VOLUME /config  
VOLUME /downloads  
  
COPY entrypoint.sh /usr/local/bin/entrypoint.sh  
RUN chmod +x /usr/local/bin/entrypoint.sh  
  
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]  
WORKDIR /app  
CMD ["python", "pyLoadCore.py", "--configdir=/config"]  

