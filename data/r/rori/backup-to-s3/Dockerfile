FROM ubuntu  
MAINTAINER rori <mail@rori.info>  
  
RUN apt-get update && \  
apt-get install -y -q python-setuptools && \  
easy_install pip && \  
pip install awscli  
  
ADD files/main.sh /main.sh  
  
RUN chmod +x /main.sh  
  
VOLUME ["/data"]  
  
ENTRYPOINT ["/main.sh"]  

