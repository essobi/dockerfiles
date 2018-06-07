FROM ubuntu  
  
RUN apt-get update \  
&& apt-get install -y whois \  
&& rm -rf /var/lib/apt/lists/*  
  
ENTRYPOINT ["/usr/bin/env", "mkpasswd"]  
  
CMD ["--method=sha-512"]  

