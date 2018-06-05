FROM alpine:latest  
MAINTAINER beardyjay <jay@beardyjay.co.uk>  
  
RUN apk add --update \  
bash \  
git \  
python \  
py-pip \  
&& rm -rf /var/cache/apk/*  
  
# Install theharvester from git along with deps  
WORKDIR /usr/share  
RUN pip install requests && git clone
https://github.com/laramies/theHarvester.git && chmod +x
theHarvester/theHarvester.py  
  
ENTRYPOINT ["/usr/share/theHarvester/theHarvester.py"]  

