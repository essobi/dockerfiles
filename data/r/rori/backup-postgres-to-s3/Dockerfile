FROM postgres:latest  
MAINTAINER rori <mail@rori.info>  
  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y curl && \  
curl -sSL https://bootstrap.pypa.io/get-pip.py | python && \  
pip install awscli  
  
ADD files/main.sh /main.sh  
  
RUN chmod +x /main.sh  
  
ENTRYPOINT ["/main.sh"]  

