FROM hashicorp/packer:0.10.0  
# Define our acceptable ansible version  
ENV ANSIBLE_VERSION 2.1.0.0  
# Import a testing edge for more recent pkgs  
RUN echo "http://dl-4.alpinelinux.org/alpine/edge/testing" >>
/etc/apk/repositories  
  
# update/install a bunch of stuffs for pythons  
RUN apk add --update py-pip build-base python-dev py-boto && rm -rf
/var/cache/apk/**/  
  
# Install ansible  
RUN pip install ansible>=${ANSIBLE_VERSION}  
  
# Set a default working dir (nice for bind mounting things inside)  
RUN mkdir /build  
WORKDIR /build  
  
# Packer needs this set:  
#
https://github.com/mitchellh/packer/blob/49067e732a66c9f7a87843a2c91100de112b21cc/provisioner/ansible/provisioner.go#L127  
ENV USER root  
  
# Set our entrypoint back to the default (gitlab-runner needs this)  
ENTRYPOINT ["/bin/sh", "-c"]  

