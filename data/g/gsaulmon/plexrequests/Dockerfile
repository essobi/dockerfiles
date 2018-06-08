FROM fedora:23  
RUN dnf install -y tar git procps \  
&& dnf clean all \  
&& curl https://install.meteor.com/ | sh \  
&& git clone https://github.com/lokenx/plexrequests-meteor.git /opt/app \  
&& mkdir -p /opt/app/.meteor/local \  
  
VOLUME ["/opt/app/.meteor/local"]  
EXPOSE 3000  
WORKDIR /opt/app  
  
ENTRYPOINT ["/usr/local/bin/meteor"]  

