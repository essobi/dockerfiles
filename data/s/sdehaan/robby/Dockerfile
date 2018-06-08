FROM praekeltfoundation/pypy-base  
  
RUN apt-get-install.sh gcc python-dev  
WORKDIR /app  
  
COPY . /app  
RUN pip install -e .  
RUN apt-get-purge.sh gcc python-dev  
  
ENTRYPOINT ["tini", "--", "/app/robby-entrypoint.sh"]  
CMD []  

