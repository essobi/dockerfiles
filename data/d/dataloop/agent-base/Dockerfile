FROM smebberson/alpine-base:2.0.0  
MAINTAINER Tom Ashley <tom@dataloop.io>  
  
# Install dataloop basic requirements  
RUN apk add --no-cache --update bash curl python python-dev py-pip gcc musl-
dev linux-headers s6  
  
ADD agent/ /opt/dataloop/agent  
  
# install pip requirements and make necessary dirs  
RUN pip install -r /opt/dataloop/agent/requirements.txt && mkdir -p
/etc/dataloop /var/log/dataloop /opt/dataloop  
  
# add run scripts  
ADD root/ /  
  
# compile and cleanup/remove py files for pyc ?  
RUN /usr/bin/python -m compileall /opt/dataloop/agent  
RUN find /opt/dataloop/agent/dataloop_agent -path
/opt/dataloop/agent/dataloop_agent/__init__.py -prune -o -name '*py' -print
-exec rm -fv {} \;  
  
# cleanup  
RUN apk del python-dev gcc linux-headers binutils binutils-libs libstdc++ gmp
isl  
  
# expose the fingerprint  
EXPOSE 8000  

