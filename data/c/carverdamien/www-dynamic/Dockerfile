FROM ubuntu  
EXPOSE 80  
CMD /bin/bash -c "while true; do echo $((RANDOM)) $(hostname) | nc -l 80 >
/dev/null; done"  
  

