FROM eeacms/varnish:4.1-6.1  
LABEL maintainer="European Environment Agency (EEA): IDM2 A-Team <eea-edw-a-
team-alerts@googlegroups.com>"  
  
ENV CACHE_SIZE="2G" \  
PARAM_VALUE="-p thread_pools=8 -p thread_pool_timeout=120 -p
thread_pool_add_delay=0.002 -p ban_lurker_sleep=0.1 -p send_timeout=3600" \  
BACKENDS="anon auth download" \  
BACKENDS_PORT="8080" \  
BACKENDS_PROBE_ENABLED="false"  
COPY varnish.vcl /etc/varnish/conf.d/  

