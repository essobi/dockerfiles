FROM python:3.6  
RUN groupadd -r sim && useradd -r -g sim sim  
  
RUN pip install
https://github.com/felipeZ/microservices/tarball/master#egg=simulator  
  
WORKDIR /app  
  
COPY app /app  
  
COPY cmd.sh /  
  
RUN ["chmod", "+x", "/cmd.sh"]  
  
USER sim  
  
  
CMD ["/cmd.sh"]  

