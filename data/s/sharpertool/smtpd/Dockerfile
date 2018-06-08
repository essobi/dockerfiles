FROM python:3.6.3-jessie  
  
ENV PYTHONUNBUFFERED 1  
EXPOSE 25  
CMD ["python", "-m", "smtpd", "-n", "-c", "DebuggingServer", "0.0.0.0:25"]  
  

