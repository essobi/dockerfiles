FROM hashicorp/packer:1.2.1  
  
RUN apk update && \  
apk upgrade && \  
apk --no-cache add "ansible<2.4" py-pip py-setuptools ca-certificates ruby
ruby-rdoc ruby-irb && \  
apk --no-cache add \--virtual .build-dependencies build-base ruby-dev && \  
pip install awscli && \  
gem install inspec && \  
apk --no-cache del .build-dependencies  
  
ADD run.sh /bin/run.sh  
  
ENTRYPOINT ["/bin/bash", "/bin/run.sh"]  

