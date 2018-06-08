FROM python:3.5-slim  
  
EXPOSE 80  
EXPOSE 443  
ENV PYTHONUNBUFFERED="1" AUTHSERVER_SSL_KEY="" AUTHSERVER_SSL_CERT=""  
CMD ["gunicorn", "-c", "gunicorn.py", "authserver.main:get_app()"]  
  
ARG base_dir="/src/authserver"  
WORKDIR ${base_dir}  
  
COPY requirements.txt ${base_dir}/requirements.txt  
RUN pip install -r requirements.txt  
  
COPY . ${base_dir}  

