FROM python:2  
MAINTAINER Simon Li "spli@dundee.ac.uk"  
RUN mkdir -p /server/cgi-bin  
RUN useradd cgi  
RUN pip install dnspython  
  
ADD run.sh /  
ADD hello.py /server/cgi-bin/hello  
  
USER cgi  
WORKDIR /server  
  
VOLUME /server/cgi-bin  
  
EXPOSE 8080  
ENTRYPOINT ["/bin/bash", "/run.sh"]  
CMD ["8080"]  

