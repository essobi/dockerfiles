# Will launch a script located in /home/borg/scripts following arguments
passed to the run command  
FROM sebcworks/borgbackup-base:1.0  
MAINTAINER Sebastien Collin <sebastien.collin@sebcworks.fr>  
  
COPY docker-borg-client-entrypoint.sh /borg-client.sh  
COPY example_script.sh /home/borg/example_script.sh  
COPY example_script2.sh /home/borg/example_script2.sh  
  
ENTRYPOINT ["/borg-client.sh"]  
CMD ["start"]

