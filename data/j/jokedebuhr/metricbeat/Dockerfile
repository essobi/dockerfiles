FROM frolvlad/alpine-glibc:alpine-3.4  
WORKDIR /metricbeat  
ENTRYPOINT [ "/metricbeat/metricbeat" ]  
CMD [ "-help" ]  
ARG VERSION=5.2.2  
RUN apk update && apk add ca-certificates openssl && update-ca-certificates \  
&& wget -O-
https://artifacts.elastic.co/downloads/beats/metricbeat/metricbeat-${VERSION}-linux-x86_64.tar.gz
| tar xz \  
&& mv metricbeat-${VERSION}-linux-x86_64/* . && rm -rf
metricbeat-${VERSION}-linux-x86_64 /var/cache/apk/*  

