FROM ubuntu:latest  
COPY abc /  
RUN chown root:root /abc  
RUN chmod -R 777 /abc  
##ENTRYPOINT ["/bin/bash"]  
RUN cp /abc /bin  
CMD ["cat /abc"]  
##RUN cat abc  
##CMD cat abc  
##RUN cat /abc  

