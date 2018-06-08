FROM debian:jessie  
  
MAINTAINER Romain THERRAT <romain42@gmail.com>  
LABEL Description="Varnish 4.0 on debian:jessie"  
  
ENV VARNISH_MAJOR=4.0  
RUN PACKAGE_DEPENDENCY="\  
apt-transport-https \  
curl \  
ca-certificates \  
" \  
&& apt-get update \  
&& apt-get install -y $PACKAGE_DEPENDENCY \  
&& curl https://repo.varnish-cache.org/GPG-key.txt | apt-key add - \  
&& echo "deb https://repo.varnish-cache.org/debian/ jessie varnish-4.0" >
/etc/apt/sources.list.d/varnish.list \  
&& apt-get update \  
&& apt-get install -y varnish \  
&& apt-get purge -y --auto-remove -o
APT::AutoRemove::RecommendsImportant=false -o
APT::AutoRemove::SuggestsImportant=false $buildDeps \  
&& rm -rf /var/lib/apt/lists/*  
  
EXPOSE 6081 6082  
ENTRYPOINT ["/usr/sbin/varnishd", "-F", "-a", "0.0.0.0:6081", "-f",
"/etc/varnish/default.vcl"]  

