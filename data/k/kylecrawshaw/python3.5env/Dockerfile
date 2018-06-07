FROM python:3.5  
ADD ./entrypoint.sh /usr/local/entrypoint.sh  
  
RUN chmod +x /usr/local/entrypoint.sh  
RUN mkdir /data  
  
ENTRYPOINT ["/usr/local/entrypoint.sh"]  
  
CMD ["python"]  

