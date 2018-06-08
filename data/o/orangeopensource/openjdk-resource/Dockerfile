FROM concourse/busyboxplus:git  
  
ADD https://github.com/stedolan/jq/releases/download/jq-1.5/jq-linux64
/usr/local/bin/jq  
RUN chmod +x /usr/local/bin/jq  
  
ADD
https://github.com/ericchiang/pup/releases/download/v0.3.9/pup_linux_amd64.zip
/usr/local/bin/pup  
RUN chmod +x /usr/local/bin/pup  
  
# add scripts  
ADD assets/ /opt/resource/  
RUN chmod +x /opt/resource/*  
  

