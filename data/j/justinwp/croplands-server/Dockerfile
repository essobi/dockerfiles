FROM justinwp/croplands-base  
  
RUN git clone https://github.com/justinwp/croplands  
RUN pip install -r /croplands/requirements.txt  
  
WORKDIR /croplands  
  
USER nobody  
  
EXPOSE 8000  
CMD gunicorn herokuapp:app -b :8000 --workers=5

