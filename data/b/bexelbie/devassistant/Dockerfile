FROM fedora  
MAINTAINER Brian (bex) Exelbierd <bex@pobox.com>  
  
# Update the container  
RUN dnf -y update && dnf clean all  
  
# Install the appropriate software  
# python3-jsonschema required for da extra validate nulecule  
RUN dnf -y install devassistant python3-jsonschema && dnf clean all  
RUN da pkg install nulecule  
  
# Setup working directory  
WORKDIR /workdir  
  
# Labels - today atomic run will not work :(  
LABEL RUN docker --rm=true \--privileged -i -t -u \${SUDO_UID}:\${SUDO_GID} -v
`pwd`:/workdir \${IMAGE}  
  
ENTRYPOINT ["/usr/bin/da"]  

