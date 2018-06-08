FROM python:alpine  
  
LABEL maintainer="Sherpany DevOps Team <devops@sherpany.com>"  
  
WORKDIR /app  
  
RUN pip install flake8 flake8-html && rm -r /root/.cache  
  
ENTRYPOINT ["flake8"]  
CMD ["/app/src"]  

