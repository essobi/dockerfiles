FROM debian:8.2  
  
# We want UTF-8 by default  
ENV LANG C.UTF-8  
  
RUN apt-get update && apt-get install -y \  
python \  
python-dev \  
python-pip \  
python-pil \  
python-psycopg2 \  
python-mysqldb \  
&& apt-get clean  
  
CMD ["python2"]  

