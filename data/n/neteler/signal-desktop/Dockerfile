FROM bitnami/minideb:stretch  
  
LABEL maintainer "Kayvan Sylvan <kayvansylvan@gmail.com>"  
  
RUN install_packages curl gnupg2 apt-transport-https ca-certificates \  
libx11-xcb1 libasound2 \  
&& curl -s https://updates.signal.org/desktop/apt/keys.asc > signal-repo.key \  
&& apt-key add signal-repo.key \  
&& echo "deb [arch=amd64] https://updates.signal.org/desktop/apt xenial main"
> \  
/etc/apt/sources.list.d/signal-xenial.list \  
&& install_packages signal-desktop  
  
ENTRYPOINT ["/usr/local/bin/signal-desktop"]  
  

