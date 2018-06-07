FROM debian:stretch-slim  
  
COPY bin/ /usr/bin/  
ENTRYPOINT ["/usr/bin/entrypoint"]  
HEALTHCHECK \--interval=10s --timeout=1s CMD ["/usr/bin/healthcheck"]  
SHELL ["/bin/bash", "-euxc"]  
WORKDIR /srv  
  
RUN apt-install ca-certificates curl gettext-base jq \  
&& rm -r /usr/bin/*gettext* /usr/share/java/libintl.jar \  
&& adduser --disabled-login --disabled-password --group --no-create-home
--quiet --system srv \  
&& mkdir -p /usr/local/etc \  
&& chown srv /srv /usr/local/etc \  
&& (find / -perm /6000 -type f -exec chmod a-s {} \; 2>/dev/null || :)  

