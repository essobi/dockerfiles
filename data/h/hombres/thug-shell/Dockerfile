FROM python:2  
MAINTAINER xirax "bad-hombres"  
WORKDIR /usr/src/  
  
RUN true \  
&& export DEBIAN_FRONTEND=noninteractive \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends git  
  
RUN git clone https://github.com/bad-hombres/thug-shell.git  
WORKDIR /usr/src/thug-shell  
  
RUN pip install --no-cache-dir docopt  
RUN pip install --no-cache-dir playsound  
  
COPY entrypoint.sh .  
ENTRYPOINT [ "./entrypoint.sh" ]  

