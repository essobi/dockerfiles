FROM debian:jessie  
  
RUN apt-get update \  
&& RUNTIME_DEPS=' \  
shellcheck \  
' \  
&& apt-get install -y --no-install-recommends ${RUNTIME_DEPS} \  
&& rm -rf /var/lib/apt/lists/*  
  
ENTRYPOINT ["shellcheck"]  

