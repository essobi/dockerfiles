FROM docker:17.12.0-ce  
FROM zenika/alpine-chrome  
FROM testcafe/testcafe  
  
ADD py_requirements.txt /  
  
USER root  
  
RUN apk --no-cache update && \  
apk --no-cache add python py-pip py-setuptools ca-certificates curl groff less
bash jq yarn && \  
pip --no-cache-dir install -r /py_requirements.txt && \  
rm -rf /var/cache/apk/*  

