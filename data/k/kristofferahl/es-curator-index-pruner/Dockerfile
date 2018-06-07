FROM bobrik/curator:5.5.1  
COPY entrypoint /  
COPY curator.yml /  
COPY actions.yml /  
  
ENTRYPOINT ["/entrypoint"]  
CMD ["--config", "/curator.yml", "/actions.yml"]  

