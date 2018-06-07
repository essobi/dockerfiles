# python:alpine is 3.{latest}  
FROM tiangolo/uwsgi-nginx:python2.7  
RUN pip install flask  
  
COPY src /src/  
  
COPY fakednf.conf /etc/nginx/conf.d/  
  
RUN chmod +x /src/start.sh  
  
# ENTRYPOINT ["python", "/src/app.py"]  
CMD ["bash","/src/start.sh"]  
  
# CMD ["nginx", "-g", "daemon off;"]  

