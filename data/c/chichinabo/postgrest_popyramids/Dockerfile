FROM ubuntu:trusty  
  
ENV POSTGREST_VERSION 0.3.1.0  
RUN apt-get update && apt-get install --no-install-recommends -y xz-utils curl
libpq-dev libgmp10 && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/*
/var/tmp/*  
  
RUN curl -L --insecure
https://github.com/begriffs/postgrest/releases/download/v${POSTGREST_VERSION}/postgrest-${POSTGREST_VERSION}-ubuntu.tar.xz
\  
| tar -xJO > /usr/local/bin/postgrest \  
&& chmod u+x /usr/local/bin/postgrest  
  
EXPOSE 8091  
COPY entrypoint.sh /  
  
CMD ["/entrypoint.sh"]  

