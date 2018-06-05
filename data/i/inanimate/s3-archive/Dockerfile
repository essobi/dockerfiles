FROM debian:jessie  
  
RUN mkdir /app && \  
apt-get update && \  
apt-get install -y -q gnupg xz-utils tar python-setuptools ca-certificates &&
\  
easy_install pip && \  
pip install awscli  
  
## Add in our main run script.  
ADD run /app/run  
## Disabling for now until I get this working.  
#ADD restore /app/restore  
# If you want to use a config, rename s3cfg.example to s3cfg  
#ADD s3cfg /root/.aws/config  
RUN chmod +x /app/run  
#RUN chmod +x /app/restore  
  
CMD ["/app/run"]  

