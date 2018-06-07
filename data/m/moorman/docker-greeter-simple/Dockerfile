FROM python:3.6-slim  
  
RUN pip3 install flask gunicorn  
  
COPY . /app  
WORKDIR /app  
  
EXPOSE 80  
ENV PYTHONUNBUFFERED=1  
CMD ["/app/entrypoint"]  

