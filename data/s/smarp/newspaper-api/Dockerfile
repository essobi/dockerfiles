FROM checksum/python-newspaper:latest  
  
RUN apk --update add linux-headers  
RUN pip install --no-cache-dir flask uwsgi  
  
COPY . .  
ENV NEWSPAPER_PORT 38765  
EXPOSE $NEWSPAPER_PORT  
CMD ["uwsgi", "--ini", "./src/wsgi.ini"]  

