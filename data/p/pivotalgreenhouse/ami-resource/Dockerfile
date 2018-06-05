# docker pull pivotalgreenhouse/ami-resource  
FROM concourse/busyboxplus:ruby  
  
RUN gem install aws-sdk -v 2.3.9 --no-document  
  
ADD bin/ /opt/resource/  
RUN chmod +x /opt/resource/*  

