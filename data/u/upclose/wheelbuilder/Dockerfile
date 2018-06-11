FROM gliderlabs/alpine:3.2  
RUN apk-install \  
python \  
python-dev \  
py-pip \  
binutils \  
libc-dev \  
gcc \  
fortify-headers \  
linux-headers \  
libffi-dev \  
postgresql-dev \  
&& pip install --no-cache virtualenv  
  
RUN virtualenv /wheel_venv  
  
# these are some setup_requires dependencies that explode on SSL checks later  
# God knows why  
# maybe because of this
https://pip.readthedocs.org/en/stable/reference/pip_install.html#controlling-
setup-requires  
RUN /wheel_venv/bin/pip install --no-cache cffi ply ipaddress enum34 six
pyasn1 idna devpi-client  
  
CMD /host/wheelbuilder/run  

