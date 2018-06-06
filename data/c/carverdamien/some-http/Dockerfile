FROM ubuntu  
EXPOSE 80  
CMD /bin/bash -c "touch /html/index.html; while true; do hostname | cat -
/html/index.html | nc -l 80 > /dev/null; done"  
VOLUME /html  

