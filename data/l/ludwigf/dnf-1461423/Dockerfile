FROM fedora:26  
# run dnf to have some cache to work with  
# and enable testing  
RUN dnf install -y 'dnf-command(config-manager)' && \  
dnf config-manager --set-enabled updates-testing && \  
dnf update -y  
  
ADD bug.py /usr/local/bin  
  
ENTRYPOINT python3 /usr/local/bin/bug.py  

