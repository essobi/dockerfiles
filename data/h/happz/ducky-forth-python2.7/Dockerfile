FROM python:2.7.11-alpine  
  
MAINTAINER Milos Prchlik <happz@happz.cz>  
  
ENV VIRTUAL_ENV=/usr/local  
ENV PYTHONUNBUFFERED=yes  
  
RUN apk update && apk add make bash wget curl jq scons git gcc musl-dev  
  
RUN wget --no-check-certificate -O /tmp/ducky-forth-latest.tar.gz
https://ducky.happz.cz/forth/ducky-forth-latest.tar.gz && tar xzf /tmp/ducky-
forth-latest.tar.gz -C / && rm -f /tmp/ducky-forth-latest.tar.gz  
RUN mkdir -p /home && wget -O /home/ducky.zip --no-check-certificate
https://github.com/happz/ducky/archive/master.zip && cd /home && unzip
ducky.zip && mv ducky-master ducky && cd /home/ducky && python setup.py
install  
  
ENTRYPOINT ["/usr/local/bin/python", \  
"-OO", \  
"/usr/local/bin/ducky-vm", \  
"--machine-config=/forth/forth.conf", \  
"--set-option=bootloader:file=/forth/ducky-forth", \  
"--set-option=device-3:streams_in=/forth/ducky-forth.f", \  
"--add-option=device-3:streams_in=<stdin>", \  
"--set-option=device-3:stream_out=<stderr>", \  
"--set-option=device-3:echo=no", \  
"--set-option=cpu:check-frames=no", \  
"--jit" \  
]  

