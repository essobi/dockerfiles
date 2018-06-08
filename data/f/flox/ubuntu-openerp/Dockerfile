FROM ubuntu:12.04  
  
MAINTAINER Florent Xicluna  
  
RUN /bin/mv /etc/apt/sources.list /etc/apt/sources.list.d/ubuntu.list \  
&& echo deb http://apt.postgresql.org/pub/repos/apt/ precise-pgdg main \  
> /etc/apt/sources.list.d/pgdg.list \  
&& mv /usr/bin/ischroot /usr/bin/chroot.orig \  
&& ln -s /bin/true /usr/bin/ischroot \  
&& export DEBIAN_FRONTEND=noninteractive LANG && apt-get update \  
&& apt-get install -y \--no-install-recommends language-pack-en \  
&& update-locale LANG=en_US.UTF-8 && . /etc/default/locale \  
&& apt-get install -y \--allow-unauthenticated pgdg-keyring \  
&& apt-get update && apt-get upgrade -y \  
&& apt-get install -y postgresql-9.3 postgresql-contrib-9.3 supervisor  
  
RUN echo deb http://nightly.openerp.com/trunk/nightly/deb/ ./ \  
> /etc/apt/sources.list.d/openerp-trunk.list \  
&& export DEBIAN_FRONTEND=noninteractive LANG=en_US.UTF-8 \  
&& apt-get update && apt-get install -y \--allow-unauthenticated openerp \  
&& service postgresql start && su - postgres -c "createuser -d openerp"  
  
ADD supervisor.conf.d/ /etc/supervisor/conf.d/  
  
EXPOSE 8069  
  
ENTRYPOINT ["/usr/bin/supervisord", "-n", "-c",
"/etc/supervisor/supervisord.conf"]

