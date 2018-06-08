FROM phase2/servicebaselight  
  
RUN apk add --update \  
python \  
python-dev \  
py-pip \  
build-base \  
&& pip install automated-ebs-snapshots \  
&& rm -rf /var/cache/apk/*  
  
ADD run.sh /run.sh  
RUN chmod +x /run.sh  
  
ENTRYPOINT ["/run.sh"]  

