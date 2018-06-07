FROM python:3.6  
MAINTAINER Inspectorio DevOps <devops@inspectorio.com>  
  
ARG DEBIAN_FRONTEND=noninteractive  
ARG PIP_NO_CACHE_DIR=1  
ARG PIP_CACHE_DIR=/tmp/  
  
ENV APP_USER app  
ENV APP_GRP app  
ENV APP_HOME /app  
ENV APP_SHELL /bin/bash  
ENV NGINX_WORKER 4  
ONBUILD ADD . "${APP_HOME}"  
ONBUILD ADD config /etc  
ONBUILD WORKDIR "${APP_HOME}"  
  
COPY requirements.txt /tmp/requirements.txt  
COPY entrypoint.sh /tmp/entrypoint.sh  
COPY config /etc/  
  
RUN groupadd "${APP_GRP}" \  
&& groupadd supervisor \  
&& useradd --create-home --home-dir "${APP_HOME}" \--shell "${APP_SHELL}"
\--gid "${APP_GRP}" "${APP_USER}" \  
&& usermod -a -G supervisor "${APP_USER}" \  
&& mv /tmp/entrypoint.sh "${APP_HOME}/entrypoint.sh" \  
&& chown -R "${APP_USER}":"${APP_GRP}" "${APP_HOME}" \  
&& apt-get -qq -y update \  
&& apt-get install -qq -o Dpkg::Options::="--force-confold" \  
-y --no-install-recommends \  
supervisor curl jq vim-nox openssh-client \  
moreutils gettext-base locales tzdata lsb-release \  
&& curl -sSL http://nginx.org/keys/nginx_signing.key | apt-key add - \  
&& echo "deb http://nginx.org/packages/$(lsb_release -is | tr '[:upper:]'
'[:lower:]')/ $(lsb_release -cs) nginx" > /etc/apt/sources.list.d/nginx.list \  
&& apt-get -qq -y update \  
&& apt-get -qq -o Dpkg::Options::="--force-confold" -y install nginx \  
&& /bin/rm -f /etc/nginx/nginx.conf.dpkg-dist
/etc/supervisor/supervisord.conf.dpkg-dist \  
&& ln -sf /dev/stdout /var/log/nginx/access.log \  
&& ln -sf /dev/stderr /var/log/nginx/error.log \  
&& rm -f /etc/nginx/conf.d/* /etc/nginx/sites-enabled/* \  
&& pip install --no-cache-dir -U -r /tmp/requirements.txt \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
WORKDIR /app  
  
EXPOSE 5000  
CMD ["/app/entrypoint.sh"]  

