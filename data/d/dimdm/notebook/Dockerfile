FROM python:3-alpine  
  
# prevent jupyter kernel crashes by using tini as a process subreaper  
ENV TINI_SUBREAPER=true  
ARG TINI_VERSION=v0.16.1  
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini-
static-amd64 /usr/bin/tini  
  
RUN apk --no-cache add --virtual runtime-dependencies \  
alpine-sdk &&\  
pip install \  
notebook \  
requests &&\  
mkdir -p /work &&\  
chmod +x /usr/bin/tini &&\  
# allow iframes embedding by relaxing CSP  
sed -i "s/\"frame-ancestors 'self'\",//g" /usr/local/lib/python$(python
--version 2>&1 | egrep -o '3\\.[0-9]+')/site-
packages/notebook/base/handlers.py &&\  
adduser -D -u 1000 notebook &&\  
chown -R notebook:notebook /work  
  
USER notebook  
EXPOSE 8888  
VOLUME /work  
WORKDIR /work  
CMD /usr/bin/tini -- jupyter notebook --ip=0.0.0.0 --no-browser
--NotebookApp.token=''  

