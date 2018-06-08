FROM ubuntu:14.04  
MAINTAINER Jerry Baker (kizbitz): 'jbaker@docker.com'  
WORKDIR /home/gyw  
  
RUN apt-get update && apt-get install -y --no-install-recommends \  
firefox \  
python-pip \  
xvfb \  
wget && \  
  
pip install --upgrade \  
beautifulsoup4 \  
click \  
pip \  
pyshorteners \  
pyvirtualdisplay \  
selenium \  
terminaltables  
  
  
RUN wget
https://github.com/mozilla/geckodriver/releases/download/v0.14.0/geckodriver-v0.14.0-linux64.tar.gz
-O /tmp/pkg.tar.gz && \  
tar -xvzf /tmp/pkg.tar.gz -C /usr/local/bin/ && \  
rm -rf /tmp/*  
  
RUN apt-get remove -y python-pip wget && \  
rm -rf /var/lib/apt/lists/*  
  
COPY . /home/gyw/  
  
ENTRYPOINT ["/home/gyw/gyw/gyw.py"]  

