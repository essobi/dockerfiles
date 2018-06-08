FROM cgswong/aws:aws  
MAINTAINER Jacob Sanford <jsanford_at_unb.ca>  
  
ENV AWS_SNS_TOPIC_ARN NULL  
ENV AWS_SNS_MESSAGE NULL  
  
COPY scripts /scripts  
  
ENTRYPOINT ["/scripts/run.sh"]  

