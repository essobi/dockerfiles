FROM debian:jessie  
  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends arping \  
&& apt-get clean  
  
COPY arping.sh /arping  
  
ENTRYPOINT ["/arping"]  

