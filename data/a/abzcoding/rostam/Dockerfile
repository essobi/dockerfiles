from python:2-alpine  
MAINTAINER Abouzar Parvan <abzcoding@gmail.com>  
COPY files /files  
RUN apk add \--no-cache git \  
&& cd /files \  
&& git clone https://github.com/abzcoding/rostam.git \  
&& apk del git \  
&& apk add \--no-cache gcc make autoconf alpine-sdk libc-dev linux-headers
python-dev tzdata \  
&& pip install --no-cache-dir -r /files/requirements.txt \  
&& cp /usr/share/zoneinfo/UTC /etc/localtime \  
&& echo "UTC" > /etc/timezone \  
&& apk del gcc make autoconf alpine-sdk libc-dev linux-headers python-dev
tzdata \  
&& rm -rf ~/.cache  
CMD [ "python", "/files/new.py" ]  

