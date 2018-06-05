FROM debian:jessie  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN set -x \  
&& apt-get -qq update \  
&& apt-get install -yq --no-install-recommends pgbouncer \  
&& apt-get purge -y --auto-remove \  
&& rm -rf /var/lib/apt/lists/*  
  
ADD entrypoint.sh ./  
  
EXPOSE 6432 5432  
ENTRYPOINT ["./entrypoint.sh"]  

