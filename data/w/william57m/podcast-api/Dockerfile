FROM python:3.6.1-onbuild  
  
ENV LC_ALL=C.UTF-8 \  
LANG=C.UTF-8 \  
FLASK_APP=/usr/src/app/api.py  
  
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]

