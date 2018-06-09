FROM fedora:23  
MAINTAINER mjs@touk.pl  
  
ENV AWS_ACCESS_KEY_ID ""  
ENV AWS_SECRET_ACCESS_KEY ""  
ENV AWS_DEFAULT_REGION ""  
ENV AWS_DEFAULT_OUTPUT text ""  
RUN dnf install -y python python-pip  
RUN pip install awscli  
  
ENTRYPOINT ["aws"]  
CMD ["--help"]  

