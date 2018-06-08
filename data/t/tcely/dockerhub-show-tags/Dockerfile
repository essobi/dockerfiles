FROM alpine:3.7  
LABEL maintainer="https://keybase.io/tcely"  
  
RUN apk --update add \  
python \  
py-requests py-yaml && \  
apk add --virtual build-deps \  
git py2-pip && \  
git clone \--recurse-submodules --single-branch
'https://github.com/HariSekhon/pytools.git' /pytools ; \  
pip install blessings bs4 ; \  
apk del --purge build-deps ; \  
rm -rf /var/cache/apk/*  
  
ENTRYPOINT ["/pytools/dockerhub_show_tags.py"]  

