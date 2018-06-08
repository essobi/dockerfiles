FROM prologic/python-runtime  
  
ENTRYPOINT ["/entrypoint.sh"]  
CMD []  
  
VOLUME /data  
  
RUN pip install irclog2html  
  
COPY entrypoint.sh /entrypoint.sh  
  
WORKDIR /data  

