FROM openlabs/docker-wkhtmltopdf-aas:latest  
RUN apt-get install -y fonts-unfonts-core  
CMD ["-b", "0.0.0.0:80", "--log-file", "-", "app:application", "--timeout",
"3600"]  

