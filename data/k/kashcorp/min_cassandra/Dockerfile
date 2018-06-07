FROM cassandra:3.3  
ENV MAX_HEAP_SIZE 64M  
ENV HEAP_NEWSIZE 12M  
  
COPY min_requirement.sh /dockerhubworkaround/min_requirement.sh  
RUN cp -r /dockerhubworkaround/* / && rm -r /dockerhubworkaround  
  
CMD ["cassandra", "-f"]  
ENTRYPOINT ["/min_requirement.sh"]  

