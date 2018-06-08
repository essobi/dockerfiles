FROM debian:jessie  
# TO flox/debian-openerp:8.0  
  
MAINTAINER Florent Xicluna  
  
# flox/debian-postgresql:9.3  
RUN apt-key adv --keyserver pool.sks-keyservers.net --recv-keys
B97B0AFCAA1A47F044F244A07FCC7D46ACCC4CF8 \  
&& echo deb http://http.debian.net/debian jessie main contrib non-free \  
> /etc/apt/sources.list.d/debian-jessie.list \  
&& echo deb http://apt.postgresql.org/pub/repos/apt/ sid-pgdg main \  
> /etc/apt/sources.list.d/pgdg.list \  
&& /bin/rm /etc/apt/sources.list \  
&& export DEBIAN_FRONTEND=noninteractive LANG \  
&& echo en_US.UTF-8 UTF-8 > /etc/locale.gen \  
&& apt-get update \  
&& apt-get install -y \--no-install-recommends apt-utils locales logrotate \  
&& update-locale LANG=en_US.UTF-8 && . /etc/default/locale \  
&& apt-get install -y postgresql-9.3 postgresql-contrib-9.3 supervisor  
  
# Install "openerp.deb"  
# Create PostgreSQL user "openerp"  
# Untar configuration "/etc/supervisor/conf.d/"  
RUN echo deb http://nightly.openerp.com/trunk/nightly/deb/ ./ \  
> /etc/apt/sources.list.d/openerp-trunk.list \  
&& export DEBIAN_FRONTEND=noninteractive LANG=en_US.UTF-8 \  
&& apt-get update && apt-get install -y \--allow-unauthenticated openerp \  
&& service postgresql start && su - postgres -c "createuser -d openerp" \  
&& echo
H4sIAIH3+VIAA+3TUU6EMBAGYJ45RS8ALbBANNk3b2HMhoUuaQIUp+2e35awyCK6RonGON8 \  
LMC1hyPTnuqTK9BzOQkmgpexOYUW9TTErT9Phai2vw30Ux3maZ3ES5R6LkjxJPJJu28Y6o3QBhHg \  
gpf5o3631P4qvzr+XStfA1XMTuso3v+EGnO12784/Zdk0/zi19ShnLPYI2+QPb/jn83/sQdZQtPe \  
vI3/yS9m2RVeRPaFGAW3EcXYi6F2Y0KPophIJHgg9F6v72kJ0JCiJO0WiPpxEw/fUnbmVfctT5xv \  
FwfZwKfuF0dJNS9uiBsOHgl2Yl4BXAnipD0pXHOBS7kXlvu3+yHUKplt0ELgOQrvNty9Kow+NrOd \  
v2Md5Tmat2hX/t6f4dev5lz3vOPRbhN+7nf8k3035Z/aeRVmcZpj/nzDlfxz5m/C7pI9rgc3j2Ub \  
S5nnI8FheLF9ld1zaOLrXH/xcYhdN/u3UIoQQQgghhBBCCCGEEEIIIYQQQtdeAHcGNHcAKAAA \  
| base64 -di | tar -xz  
  
# Declare volumes for PostgreSQL data and logs  
VOLUME ["/var/lib/postgresql", "/var/log/postgresql"]  
  
# Expose HTTP port  
EXPOSE 8069  
  
# Autostart supervisor daemon  
ENTRYPOINT ["/usr/bin/supervisord", "-n", "-c",
"/etc/supervisor/supervisord.conf"]

