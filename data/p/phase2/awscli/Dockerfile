FROM phase2/servicebase  
  
RUN yum install -y python-crypto python-pip && \  
pip install awscli && \  
mkdir /work  
  
WORKDIR /work  
  
ENTRYPOINT ["aws"]  
CMD ["help"]  

