FROM elasticsearch:5.6.3  
  
RUN bin/elasticsearch-plugin install \--batch \--silent discovery-ec2 && \  
bin/elasticsearch-plugin install \--batch \--silent repository-s3  

