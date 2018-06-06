FROM python:3.6  
RUN pip install isso && mkdir /data  
  
COPY entrypoint.sh /entrypoint.sh  
  
HEALTHCHECK CMD ["wget", "-qO", "/dev/null",
"http://127.0.0.1/js/embed.min.js"]  
  
ENTRYPOINT ["/entrypoint.sh"]  

