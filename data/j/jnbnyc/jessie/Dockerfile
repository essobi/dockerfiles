FROM debian:jessie  
  
  
ADD install-apts.sh /usr/local/sbin/install-apts  
ADD remove-apts.sh /usr/local/sbin/remove-apts  
  
ENV BASE_INSTALLED_PACKAGES "ca-certificates curl wget vim less locales
dnsutils tcpdump pypy"  
RUN install-apts ${BASE_INSTALLED_PACKAGES}

