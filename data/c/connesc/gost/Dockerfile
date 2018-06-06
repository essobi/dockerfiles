FROM busybox:1.27-glibc  
RUN GOST_VERSION=2.4 \  
&& wget -O -
"https://github.com/ginuerzh/gost/releases/download/v${GOST_VERSION}/gost_${GOST_VERSION}_linux_amd64.tar.gz"
| tar xz \  
&& mv "gost_${GOST_VERSION}_linux_amd64/gost" /bin/gost \  
&& rm -rf "gost_${GOST_VERSION}_linux_amd64"  
ENTRYPOINT ["gost"]  

