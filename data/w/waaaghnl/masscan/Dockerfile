FROM waaaghnl/ubuntu:latest  
MAINTAINER docker@waaagh.nl  
  
ENV WORKSERVER=scantheweb.org  
ENV KEY=12345  
  
RUN apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y masscan jq  
  
  
ADD worker.sh /root/  
  
RUN chmod +x /root/worker.sh  
  
ENTRYPOINT ["/root/worker.sh"]

