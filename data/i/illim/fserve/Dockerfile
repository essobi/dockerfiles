FROM ubuntu:precise  
  
ENV RUST_LOG="fserve=info"  
RUN apt-get update && apt-get install -y curl  
  
RUN curl -o /tmp/fserve -skL
https://github.com/illim/fserve/releases/download/v0.1.7/fserve \  
&& chmod +x /tmp/fserve  
  
CMD /tmp/fserve  

