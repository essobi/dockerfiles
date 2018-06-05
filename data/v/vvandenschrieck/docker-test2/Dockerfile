FROM docker/whalesay:latest  
RUN apt-get -y update && apt-get install -y fortunes  
COPY test.txt /tmp/  
CMD cat /tmp/test.txt | cowsay  

