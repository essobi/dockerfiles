FROM debian:stretch  
  
LABEL maintainer=az@zok.xyz \  
version="1.0"  
  
RUN mkdir -p /kopano/repo && mkdir -p /kopano/data  
WORKDIR /kopano/repo  
  
ADD z-push-GPG.key /kopano/repo  
  
ENV DEBIAN_FRONTEND noninteractive  
  
# define timezone  
ENV TZ=Europe/Berlin  
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone  
  
# install basic utilities  
RUN apt-get update && apt-get install -y lynx apt-utils curl crudini gpg && rm
-rf /var/cache/apt /var/lib/apt/lists  
  
# get kopano packages  
RUN curl -L `lynx -listonly -nonumbers -dump
https://download.kopano.io/community/core:/ | grep Debian_9.0-amd64.tar.gz` |
tar xzf - --strip-components 1  
RUN curl -L `lynx -listonly -nonumbers -dump
https://download.kopano.io/community/webapp:/ | grep Debian_9.0-all.tar.gz` |
tar xzf - --strip-components 1  
  
# create and add repositories  
RUN apt-ftparchive packages . | gzip -9c > Packages.gz && echo "deb
[trusted=yes] file:/kopano/repo ./" > /etc/apt/sources.list.d/kopano.list; \  
echo "deb http://repo.z-hub.io/z-push:/final/Debian_9.0/ /" >
/etc/apt/sources.list.d/zpush.list; \  
apt-key add /kopano/repo/z-push-GPG.key  
  
# install base components  
RUN apt-get update && apt-get install -y --no-install-recommends \  
kopano-common \  
python-kopano \  
moreutils \  
&& rm -rf /var/cache/apt /var/lib/apt/lists  
  
RUN curl -L -o /usr/local/bin/dumb-init https://github.com/Yelp/dumb-
init/releases/download/v1.2.0/dumb-init_1.2.0_amd64  
RUN chmod a+x /usr/local/bin/dumb-init  
  
ADD kcconf.py /kopano/kcconf.py  
  
ENTRYPOINT ["/usr/local/bin/dumb-init", "--"]

