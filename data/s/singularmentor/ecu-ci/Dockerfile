FROM meteorhacks/meteord:base  
MAINTAINER infra@singularmentor.com.ar  
  
RUN ["apt-get", "update"]  
RUN ["apt-get", "install", "curl", "openssh-client", "git", "rsync", "-y"]  
RUN ["bash", "/opt/meteord/lib/install_meteor.sh"]  
  
ENTRYPOINT []  

