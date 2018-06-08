FROM buildpack-deps:jessie  
  
RUN apt-get update && apt-get install -y \  
mysql-client \  
&& rm -rf /var/lib/apt/lists/*  
  
WORKDIR /app  
ADD ./import.sh ./import.sh  
  
CMD [ "bash" ]

