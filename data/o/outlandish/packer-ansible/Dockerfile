FROM williamyeh/ansible:ubuntu16.04  
# Define our acceptable ansible version  
ENV PACKER_VERSION=1.1.1  
ENV
PACKER_SHA256SUM=822fe76c2dfe699f187ef8c44537d10453a1545db620e40b345cf6991a690f7d  
  
RUN apt-get update -y && apt-get install -y git bash wget openssl zip  
  
ADD
https://releases.hashicorp.com/packer/${PACKER_VERSION}/packer_${PACKER_VERSION}_linux_amd64.zip
./  
ADD
https://releases.hashicorp.com/packer/${PACKER_VERSION}/packer_${PACKER_VERSION}_SHA256SUMS
./  
  
RUN sed -i '/.*linux_amd64.zip/!d' packer_${PACKER_VERSION}_SHA256SUMS  
RUN sha256sum -c --status packer_${PACKER_VERSION}_SHA256SUMS  
RUN unzip packer_${PACKER_VERSION}_linux_amd64.zip -d /bin  
RUN rm -f packer_${PACKER_VERSION}_linux_amd64.zip  
  
RUN groupadd -g 999 appuser && \  
useradd -r -u 999 -g appuser appuser  
  
# Set a default working dir (nice for bind mounting things inside)  
RUN mkdir /build && \  
chown -R appuser:appuser /build && \  
mkdir /home/appuser && \  
chown -R appuser:appuser /home/appuser  
  
USER appuser  
  
WORKDIR /build  
  
# Packer needs this set:  
#
https://github.com/mitchellh/packer/blob/49067e732a66c9f7a87843a2c91100de112b21cc/provisioner/ansible/provisioner.go#L127  
ENV USER appuser  
  
# Set our entrypoint back to the default (gitlab-runner needs this)  
ENTRYPOINT []  

