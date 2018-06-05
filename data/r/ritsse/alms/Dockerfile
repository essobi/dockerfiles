FROM python:3-onbuild  
COPY ./ /usr/src/app  
  
RUN pip install .  
  
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]  

