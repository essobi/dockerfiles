FROM python:2.7  
MAINTAINER Rick Moran <moran@crowbits.com>  
  
RUN \  
pip install mitmproxy && \  
curl -o /usr/local/bin/read_dumpfile
https://raw.githubusercontent.com/mitmproxy/mitmproxy/master/examples/read_dumpfile
&& \  
chmod 755 /usr/local/bin/read_dumpfile && \  
rm -Rf ~/.cache/pip /tmp/pip_build_root  
  
EXPOSE 8080  
ENTRYPOINT ["mitmdump"]  

