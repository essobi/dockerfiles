From debian:jessie  
RUN apt-get update && apt-get install -y libssl-dev libffi-dev python-dev
build-essential curl git vim  
ADD auto_install.py /install.py  
RUN /install.py  
RUN /root/bin/az --help  

