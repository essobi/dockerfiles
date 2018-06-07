FROM python:2.7  
RUN apt-get update \  
&& apt-get install --no-install-recommends -y openjdk-7-jre-headless ruby  
  
RUN gem install --no-document s3_website \  
&& s3_website install  
  
RUN pip install grow  
  
VOLUME ["/website", "/config"]  
  
WORKDIR /website  
  
ENTRYPOINT ["bash"]  

