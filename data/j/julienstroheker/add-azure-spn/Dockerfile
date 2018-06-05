FROM azuresdk/azure-cli-python  
  
ADD src/* /usr/local/bin/azaddspn.sh  
  
RUN chmod +x /usr/local/bin/azaddspn.sh  
  
ENTRYPOINT ["/usr/local/bin/azaddspn.sh"]  

