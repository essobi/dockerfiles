FROM python:2-onbuild  
EXPOSE 8000  
CMD ["gunicorn", "-w4", "-b", "0.0.0.0", "app:app"]  

