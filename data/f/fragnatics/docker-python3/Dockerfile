FROM docker.io/project31/aarch64-alpine-qemu:3.5-7  
RUN [ "cross-build-start" ]  
  
MAINTAINER Frank Gnad <frank.gnad@fragnatics.de>  
RUN apk add --no-cache python3 && \  
python3 -m ensurepip && \  
rm -r /usr/lib/python*/ensurepip && \  
pip3 install --upgrade pip setuptools && \  
if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi && \  
if [[ ! -e /usr/bin/python ]]; then ln -sf /usr/bin/python3 /usr/bin/python;
fi && \  
rm -r /root/.cache  
  
CMD [ "python", "--version" ]  
  
RUN [ "cross-build-end" ]  

