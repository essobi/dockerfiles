FROM debian:stretch  
  
WORKDIR /usr/src/app  
  
COPY . .  
  
RUN apt update \  
&& apt install -y python3 \  
python3-dev \  
python3-setuptools \  
python3-pip \  
python3-yaml \  
python3-pika \  
python3-requests \  
python3-click \  
python3-pyclamd \  
python3-aiohttp  
RUN python3 ./setup.py develop  
  
ENV LC_ALL=C.UTF-8  
ENV LANG C.UTF-8  
CMD ["/usr/local/bin/antivirus", "webserver"]

