FROM debian:jessie  
  
RUN apt-get update && apt-get install -y qemu-kvm wget git unzip make bsdtar  
  
ADD https://releases.hashicorp.com/packer/0.10.1/packer_0.10.1_linux_amd64.zip
./  
  
RUN unzip packer_0.10.1_linux_amd64.zip -d /bin  
  
#yaml2json is a build of github.com/buildkite/yaml2json, included because we
use yaml files becuase you can put comments in them.  
COPY yaml2json /usr/bin/yaml2json  
  
ENTRYPOINT "/bin/bash"  

