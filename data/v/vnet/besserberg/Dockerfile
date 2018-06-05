# vim: set syntax=dockerfile:  
FROM python:3.6  
LABEL maintainer "db@vnet.sk"  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update \  
&& apt-get install -y \  
xvfb \  
ghostscript \  
ttf-dejavu \  
&& rm -rf /var/lib/apt/lists/*  
  
ADD /vendor/wkhtmltopdf.tar.xz /usr/bin  
  
COPY ./requirements.txt /tmp/requirements.txt  
  
RUN pip install -r /tmp/requirements.txt  
  
COPY ./wkhtmltopdf.sh /usr/bin/wkhtmltopdf.sh  
  
RUN chmod a+x /usr/bin/wkhtmltopdf.sh  
RUN ln -s /usr/bin/wkhtmltopdf.sh /usr/local/bin/wkhtmltopdf  
  
COPY ./besserberg /opt/besserberg  
  
RUN useradd -s /bin/bash besserberg  
USER besserberg  
  
WORKDIR /opt/besserberg  
  
ENV PYTHONPATH /opt:$PYTHONPATH  
  
CMD ["gunicorn", "-w", "2", "-b", "0.0.0.0:8000", "besserberg.app:app"]  

