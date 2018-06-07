FROM fedora  
  
RUN dnf install -y --setopt=override_install_langs=en --setopt=tsflags=nodocs
varnish redhat-rpm-config && rm -rf /var/cache/yum  
ADD . /srv/  
  
VOLUME ["/var/lib/varnish"]  
  
EXPOSE 6081 6082  
CMD ["/srv/run.sh"]  

