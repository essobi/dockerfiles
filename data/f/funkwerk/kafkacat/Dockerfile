FROM ubuntu:14.04  
MAINTAINER info@funkwerk-itk.com  
  
# TODO: do not use an unversioned binary, reference a version!  
COPY kafkacat /bin/kafkacat  
RUN chmod +x /bin/kafkacat  
  
ENTRYPOINT ["/bin/kafkacat"]  
CMD ["--help"]  

