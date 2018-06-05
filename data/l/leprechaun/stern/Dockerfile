FROM alpine  
  
ADD https://github.com/wercker/stern/releases/download/1.5.1/stern_linux_amd64
/usr/local/bin/stern  
RUN chmod 755 /usr/local/bin/stern  
  
CMD ["stern", "'.*'", "--all-namespaces", "--tail", "1" ]  

