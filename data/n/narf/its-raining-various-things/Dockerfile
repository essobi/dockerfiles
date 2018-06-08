# ubuntu 16.04  
FROM
ubuntu@sha256:a0ee7647e24c8494f1cf6b94f1a3cd127f423268293c25d924fbe18fd82db5a4  
  
RUN apt-get update --fix-missing \  
&& \  
apt-get install -yy \  
ffmpeg \  
festival \  
&& rm -rf /var/lib/apt/lists/*  
  
COPY ./media /media  
COPY ./bin/run.sh /run.sh  
RUN chmod +x /run.sh  
  
ENTRYPOINT ["/bin/bash", "/run.sh"]  

