FROM debian:jessie  
  
LABEL maintainer="David Galoyan"  
  
RUN apt-get update && apt-get install -y wget && \  
wget --no-check-certificate
https://raw.github.com/Lozy/danted/master/install.sh -O install.sh && \  
bash install.sh --port=27637 && \  
rm install.sh && \  
rm -rf /var/lib/apt/lists/*  
  
ADD entrypoint.sh /  
ADD sockd.conf /etc/danted/  
  
EXPOSE 1080 1080/udp  
  
ENTRYPOINT [ "/entrypoint.sh" ]  

