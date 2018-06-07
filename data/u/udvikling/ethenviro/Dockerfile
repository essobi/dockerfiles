FROM python:2.7.13  
ENV DEBIAN_FRONTEND noninteractive  
COPY requirements.conf /tmp/  
RUN apt-get update \  
&& apt-get install -y mysql-server --no-install-recommends \  
&& apt-get --assume-yes install netcat \  
&& apt-get clean \  
&& pip install -r /tmp/requirements.conf \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN echo "Europe/Copenhagen" > /etc/timezone  
RUN dpkg-reconfigure -f noninteractive tzdata  
RUN mkdir -p /src/pyflask  
COPY ./*.py /src/  
COPY ./*.sh /src/  
  
ENTRYPOINT ["/bin/bash", "/src/entrypoint.sh"]  

