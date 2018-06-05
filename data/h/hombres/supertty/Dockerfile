FROM python:2  
MAINTAINER xirax "bad-hombres"  
WORKDIR /usr/src/  
  
RUN true \  
&& export DEBIAN_FRONTEND=noninteractive \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends \  
git \  
netcat  
  
RUN git clone https://github.com/bad-hombres/supertty.git  
WORKDIR /usr/src/supertty  
  
RUN pip install --no-cache-dir docopt  
  
COPY entrypoint.sh .  
ENTRYPOINT [ "./entrypoint.sh" ]  

