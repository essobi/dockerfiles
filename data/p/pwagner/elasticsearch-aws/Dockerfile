FROM elasticsearch:2.3  
RUN plugin install cloud-aws  
RUN plugin install lmenezes/elasticsearch-kopf  
  
COPY elasticsearch-aws.sh /elasticsearch-aws.sh  
CMD [ "/elasticsearch-aws.sh" ]  
  

