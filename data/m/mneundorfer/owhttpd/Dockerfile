FROM debian:stretch  
LABEL AUTHOR="Maximilian Neundorfer <mail@mneundorfer.de>"  
  
RUN apt-get update && \  
apt-get install -y owhttpd  
  
EXPOSE 2121  
ENTRYPOINT [ "owhttpd", "-p", "2121", "--foreground" ]

