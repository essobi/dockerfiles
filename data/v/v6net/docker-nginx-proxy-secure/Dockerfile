FROM jwilder/nginx-proxy  
  
MAINTAINER cougar@random.ee  
  
RUN apt-get update \  
&& apt-get install -y -q --no-install-recommends \  
patch \  
&& apt-get clean \  
&& rm -r /var/lib/apt/lists/*  
  
COPY nginx.tmpl.diff /app/  
RUN patch -p0 < nginx.tmpl.diff  

