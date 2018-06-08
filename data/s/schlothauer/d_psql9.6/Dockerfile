FROM postgres:9.5  
COPY scripts/import.sh /import.sh  
  
ENTRYPOINT ["/import.sh"]  
CMD ["postgres"]  
  

