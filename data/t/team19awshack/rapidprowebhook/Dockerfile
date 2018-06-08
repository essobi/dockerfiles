FROM python:2.7  
COPY . /opt  
WORKDIR /opt  
  
RUN mkdir -p $(python -c 'import site; site._script()' \--user-site) && pwd >>
$(python -c 'import site; site._script()' \--user-site)/custom.pth  
RUN pip install -Ur requirements.txt  
  
EXPOSE 8000  
CMD ["gunicorn", "-b=0.0.0.0:8000", "app:app"]  

