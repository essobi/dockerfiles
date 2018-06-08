FROM python  
  
COPY test.py /test.py  
  
RUN chmod +x /test.py  
  
ENTRYPOINT [ "python", "/test.py", "-name", "alice", "-f" ]  
  
CMD [ "-age", "30" ]  

