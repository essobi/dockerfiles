FROM docker:1.10.3  
MAINTAINER NHS Digital Delivery Centre, CIS Team. Email: HSCIC.DL-CIS@nhs.net  
  
RUN apk update && \  
apk upgrade && \  
apk add --no-cache bash util-linux vim curl jq  
  
VOLUME /var/run/docker.sock:/var/run/docker.sock  
  
COPY start.sh /tmp/start.sh  
COPY .bashrc /root/.bashrc  
  
RUN chmod +x /tmp/start.sh  
  
CMD /tmp/start.sh  

