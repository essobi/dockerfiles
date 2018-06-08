# IDCF cloudstack-api v0.10  
# docker run --rm pottava/idcf-cli --help  
# docker run --rm -v $HOME/.idcfrc:/root/.idcfrc pottava/idcf-cli
listVirtualMachines -t id,name,group,state  
FROM pottava/python:2.7  
RUN apk --no-cache add --virtual build-dependencies build-base libxml2
libxml2-dev libxslt-dev py-pip git python-dev \  
&& apk --no-cache add py-setuptools libxslt \  
&& pip install git+https://github.com/idcf/cloudstack-api@v0.10.2 \  
&& apk del --purge build-dependencies  
  
ENTRYPOINT ["/usr/bin/cloudstack-api"]  
CMD ["--version"]  

