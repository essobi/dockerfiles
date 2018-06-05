from fedora:latest  
RUN dnf groupinstall -y 'Development Tools' && dnf -y install inotify-tools
dnf-plugins-core rpm-build && dnf clean all  
  
COPY watch.sh /  
LABEL RUN='docker run -d -v /tmp/fedora/rpms:/rpms:rw,Z IMAGE sh /watch.sh'  

