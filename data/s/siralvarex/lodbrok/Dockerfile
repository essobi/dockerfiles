FROM ubuntu-debootstrap:14.04  
  
RUN apt-get update && apt-get install -y libsqlite3-0 openssl \  
&& openssl genrsa -out _.marathon.mesos.key 2048 \  
&& openssl req -new -x509 -key _.marathon.mesos.key -out _.marathon.mesos.cert
-days 3650 -subj /CN=\\*.marathon.mesos \  
&& cat _.marathon.mesos.key > /haproxy.pem \  
&& cat _.marathon.mesos.cert >> /haproxy.pem && rm -f *marathon.mesos.* \  
&& apt-get purge -y --auto-remove $buildDeps \  
&& rm -rf /var/lib/apt/lists/*  
  
ADD lodbrok /  
CMD ["/lodbrok"]  

