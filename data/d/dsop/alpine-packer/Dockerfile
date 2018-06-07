FROM dsop/alpine-base  
  
ENV PACKER_VERSION 0.11.0  
RUN cd /usr/local/bin && \  
curl -L
https://releases.hashicorp.com/packer/${PACKER_VERSION}/packer_${PACKER_VERSION}_linux_amd64.zip
-o packer_${PACKER_VERSION}_linux_amd64.zip && \  
unzip packer_${PACKER_VERSION}_linux_amd64.zip && \  
rm packer_${PACKER_VERSION}_linux_amd64.zip  
  
RUN apk --update add dbus python py2-pip && \  
pip install awscli && \  
apk --purge -v del py2-pip && \  
rm -rf /var/cache/apk/*  
  
WORKDIR /work  
  
CMD ["/bin/bash"]  

