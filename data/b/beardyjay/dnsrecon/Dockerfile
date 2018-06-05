FROM alpine:latest  
MAINTAINER beardyjay <jay@beardyjay.co.uk>  
  
RUN apk add --update \  
bash \  
git \  
python \  
py-pip \  
&& rm -rf /var/cache/apk/*  
  
# Install dnsrecon from git along with deps  
WORKDIR /usr/share  
RUN pip install dnspython netaddr && git clone
https://github.com/darkoperator/dnsrecon.git  
  
ENTRYPOINT ["/usr/share/dnsrecon/dnsrecon.py"]  

