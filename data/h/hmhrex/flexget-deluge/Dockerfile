FROM alpine:3.5  
RUN \  
# Install python and pip  
apk add \--no-cache \  
py2-pip \  
python2 && \  
  
# Install deluge  
apk add \--no-cache \  
\--repository http://nl.alpinelinux.org/alpine/edge/testing \  
deluge && \  
  
# Make sure pip is updated  
pip install --no-cache-dir -U \  
pip && \  
  
# Install pytest-runner ignoring SSL  
pip install --index-url=http://pypi.python.org/simple/ --trusted-host
pypi.python.org \  
pytest-runner && \  
  
# Install flexget  
pip install --no-cache-dir \  
flexget  
  
VOLUME ["/flexget"]  
  
WORKDIR /flexget  
  
CMD rm -f /flexget/.config-lock && flexget daemon start  

