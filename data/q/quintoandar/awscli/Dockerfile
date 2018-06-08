FROM python:3  
RUN apt-get update && apt-get install -y groff  
  
RUN pip install awscli==1.14.*  
  
ADD entrypoint.sh /  
  
WORKDIR /workspace  
  
ENTRYPOINT [ "/entrypoint.sh" ]  
  
CMD help

