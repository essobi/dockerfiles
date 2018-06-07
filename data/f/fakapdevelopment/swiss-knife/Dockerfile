FROM maven  
  
RUN apt-get update && apt-get install -y python python-dev python-pip \  
&& pip install --upgrade pip  
  
# Node  
RUN curl -sL https://deb.nodesource.com/setup_7.x | bash - \  
&& apt-get install -y nodejs  
  
# AWS CLI  
RUN pip install awscli  
  
# Artifacts  
COPY artifacts /opt/artifacts  
RUN ln -s /opt/artifacts/* /usr/bin/  
  
WORKDIR /root  
COPY .m2 .m2  
COPY docker-entrypoint.sh /usr/local/bin/  
  
ENTRYPOINT ["docker-entrypoint.sh"]  

