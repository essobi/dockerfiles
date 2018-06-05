FROM postgres:9.5  
RUN apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y -q curl gnupg xz-utils
ca-certificates  
  
RUN curl -sSL https://bootstrap.pypa.io/get-pip.py | python  
RUN pip install awscli  
  
ADD run.sh /app/run.sh  
RUN chmod +x /app/run.sh  
  
CMD ["/app/run.sh"]  

