#  
# Debian 8.1 (Thai mirror) image  
#  
  
FROM debian:8.1  
  
# Change mirror  
RUN sed -i "s/httpredir.debian.org/ftp.th.debian.org/" /etc/apt/sources.list  
  
#  
# Build command:  
# docker build -t "sungsit/debian:thai-mirror" .  
#  
# Test command:  
# docker run -it --rm "sungsit/debian:thai-mirror" echo "Hello Debian (thai-
mirror)!"  
#  

