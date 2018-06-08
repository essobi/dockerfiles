from debian:wheezy  
  
RUN apt-get update && apt-get -y install man funny-manpages && rm -rf
/var/lib/apt/lists/*  
  
ENTRYPOINT ["/usr/bin/man"]  
  
CMD ["man]  

