FROM bitnami/minideb:jessie  
  
RUN echo "\033[36m === Install NodeJS === \033[0m" \  
&& set -x \  
&& export DEBIAN_FRONTEND=noninteractive \  
&& install_packages \  
curl \  
ca-certificates \  
apt-transport-https \  
&& curl -s https://deb.nodesource.com/gpgkey/nodesource.gpg.key | apt-key add
- \  
&& echo 'deb https://deb.nodesource.com/node_7.x jessie main' >>
/etc/apt/sources.list.d/node.list \  
&& echo 'deb-src https://deb.nodesource.com/node_7.x jessie main' >>
/etc/apt/sources.list.d/node.list \  
&& install_packages nodejs \  
&& npm install -g harp \  
&& apt-get -y purge \  
curl \  
apt-transport-https \  
&& apt-get -y autoremove \  
&& apt-get clean \  
&& rm /etc/apt/sources.list.d/node.list  
  
COPY ./tools/docker-entrypoint /entrypoint.sh  
COPY ./tools/suexec.bin /usr/local/bin/suexec  
  
RUN echo "\033[36m === Setup binary === \033[0m" \  
&& set -x \  
&& chmod +x \  
/entrypoint.sh \  
/usr/local/bin/suexec \  
&& groupadd -r harp \  
&& useradd -r -g harp harp  
  
VOLUME ["/srv/web", "/srv/build"]  
EXPOSE 9000  
  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["serve"]

