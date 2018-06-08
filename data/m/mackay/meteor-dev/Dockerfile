FROM debian:jessie  
  
USER root  
  
RUN set -x \  
&& apt-get update && apt-get install -y --no-install-recommends \  
ca-certificates \  
curl \  
vim \  
locales \  
git \  
make \  
build-essential \  
automake \  
autoconf \  
nasm \  
python \  
libpng-dev \  
&& localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias
en_US.UTF-8 \  
&& rm -rf /var/lib/apt/lists/* \  
&& groupadd --gid 1000 sprout \  
&& useradd --uid 1000 \--gid sprout --shell /bin/bash --create-home sprout \  
&& echo "alias l='ls -laFHh'" > /home/sprout/.bash_aliases \  
&& mkdir -p /work/app/src /work/libs /work/npm \  
&& echo "prefix = /work/npm" > /home/sprout/.npmrc \  
&& chown -R sprout:sprout /home/sprout /work \  
&& echo fs.inotify.max_user_watches=524288 > /etc/sysctl.d/increase-
watches.conf \  
&& sysctl -p  
  
ENV LANG en_US.utf8  
ENV METEOR_LOG=debug  
ENV METEOR_OFFLINE_CATALOG=1  
  
USER sprout  
  
RUN set -x \  
&& curl https://install.meteor.com/ | sh \  
&& METEOR_LOG=debug METEOR_OFFLINE_CATALOG=1 /home/sprout/.meteor/meteor
create /work/app/src --release 1.6.0.1 \  
&& rm -rf /work/app/src  
  
WORKDIR /work/app/src  
ENTRYPOINT ["/home/sprout/.meteor/meteor"]  
CMD ["run"]  

