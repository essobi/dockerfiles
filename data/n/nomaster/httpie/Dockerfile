FROM python:alpine  
RUN pip install httpie  
RUN adduser -Dh /home/httpie httpie  
USER httpie  
ENTRYPOINT ["/usr/local/bin/http"]  

