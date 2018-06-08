FROM ubuntu:xenial  
  
RUN apt-get update -q \  
&& apt-get install -q -y salt-minion openssh-client iproute2 \  
&& rm -rf /var/lib/apt/lists/*  
  
ADD run-on-host /usr/local/bin/run-on-host  
ADD entrypoint.sh /  
  
CMD ["/entrypoint.sh"]  

