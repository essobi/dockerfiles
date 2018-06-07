FROM wilkesystems/steamcmd:ubuntu  
  
COPY entrypoint.sh /entrypoint.sh  
  
RUN useradd -ms /bin/bash newuser && mkdir /server && chown newuser:newuser
/server  
USER newuser  
WORKDIR /server  
  
ENTRYPOINT ["/entrypoint.sh"]  
CMD [""]  

