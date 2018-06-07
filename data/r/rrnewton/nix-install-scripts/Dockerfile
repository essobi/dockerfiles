# This Dockerfile simply confirms that our script is sufficient in a  
# BARE ubuntu environment.  
FROM ubuntu:14.04  
RUN apt-get update  
RUN apt-get install -y curl  
  
# When running the install script as root, I need the nixbld group to  
# pre-exist [2016.05.14]:  
RUN addgroup nixbld  
RUN useradd -c "Nix build user $n" \  
-d /var/empty -g nixbld -G nixbld -M -N -r -s "$(which nologin)" \  
nixbld01;  
# This is also expected by the nix install script;  
ENV USER root  
  
# ------------------------------------------------------------  
ADD . /scripts  
  
RUN /scripts/single_user_install_all.sh  
  
RUN /nix/var/nix/profiles/default/bin/nix-env -q  
  
ENV PATH $PATH:/nix/var/nix/profiles/default/bin/  
  
# I'm not sure why this is needed, because it should have already been run  
# by the installer:  
RUN nix-env -i $(find /nix/store -name ca-bundle.crt)  

