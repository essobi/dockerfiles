FROM openlabs/docker-wkhtmltopdf-aas  
  
EXPOSE 80  
ENTRYPOINT ["usr/local/bin/gunicorn"]  
CMD ["-b", "0.0.0.0:80", "-t", "180", "--log-file", "-", "app:application"]

