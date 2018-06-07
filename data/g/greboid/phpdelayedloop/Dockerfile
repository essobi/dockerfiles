FROM php:7.2-cli  
  
RUN apt-get update \  
&& apt-get install python -y \  
&& rm -rf /var/lib/apt/lists/*  
  
COPY entrypoint.py /usr/local/bin/entrypoint.py  
  
RUN groupadd -g 999 phpuser && \  
useradd -r -u 999 -g phpuser phpuser  
USER phpuser  
  
WORKDIR ["/app"]  
VOLUME ["/app"]  
  
ENTRYPOINT ["/usr/local/bin/entrypoint.py"]  

