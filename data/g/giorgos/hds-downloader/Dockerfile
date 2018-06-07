FROM debian:latest  
  
WORKDIR /output  
COPY wrapper.sh /app/  
  
RUN apt-get update && apt-get install --no-install-recommends -y php5-cli
php5-curl php5-mcrypt && rm -rf /var/lib/{apt,dpkg,cache,log}  
  
ADD https://raw.githubusercontent.com/K-S-V/Scripts/master/AdobeHDS.php
/app/AdobeHDS.php  
  
ENTRYPOINT ["/app/wrapper.sh"]  

