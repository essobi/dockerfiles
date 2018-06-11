# VERSION 1.0  
FROM python:2-slim  
  
MAINTAINER Jianshen Liu <jliu120@ucsc.edu>  
  
RUN apt-get update \  
&& apt-get install -y python-twisted  
  
# Clean Up  
RUN apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
WORKDIR /root  
EXPOSE 80  
ENTRYPOINT ["twistd", "-n", "web"]  
CMD ["-p", "80", "--path", "."]  

