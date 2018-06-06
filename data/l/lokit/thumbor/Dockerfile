FROM python:2  
RUN pip install --no-cache-dir \  
thumbor==6.1.1 \  
&& rm -rf ~/.cache  
  
EXPOSE 8888  
COPY /docker-entrypoint.sh /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["thumbor"]  

