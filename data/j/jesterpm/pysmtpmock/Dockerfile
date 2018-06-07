FROM debian:jessie  
  
RUN apt-get update && apt-get -y install python  
  
EXPOSE 25  
CMD ["python", "-m", "smtpd", "-n", "-c", "DebuggingServer", "0.0.0.0:25"]  

