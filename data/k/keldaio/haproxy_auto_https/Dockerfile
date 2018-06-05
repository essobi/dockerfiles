FROM haproxy:1.8  
RUN apt-get update && apt-get install -y \  
certbot \  
&& rm -rf /var/lib/apt/lists/*  
COPY ./glue.py /  
ENV PYTHONUNBUFFERED=true  
ENTRYPOINT ["python", "glue.py"]  

