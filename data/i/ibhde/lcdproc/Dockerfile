FROM debian:buster-slim  
  
EXPOSE 13666  
  
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install --no-
install-recommends -y lcdproc lcdproc-extra-drivers  
  
CMD ["LCDd", "-f", "-s", "no", "-a", "0.0.0.0"]  

