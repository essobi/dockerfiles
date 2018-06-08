FROM ubuntu:latest  
  
MAINTAINER Tomokazu Kiyohara "tomokazu.kiyohara@gmail.com"  
# RUN apt-get update  
ADD bin/infinity_sleep.sh /usr/local/bin/infinity_sleep.sh  
RUN chmod +x /usr/local/bin/infinity_sleep.sh  
  
CMD [ "/usr/local/bin/infinity_sleep.sh" ]  

