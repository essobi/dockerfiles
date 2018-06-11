FROM debian:jessie  
  
WORKDIR /app  
ADD . /app  
  
# ENV ACCESS_TOKEN syntesys  
# ENV SECRET_TOKEN xyz  
# Define environment variable  
ENV NAME Voidp34r  
  
RUN apt update && apt -y upgrade  
RUN apt install -y nginx  
#RUN apt-get install -y cmatrix  
  
COPY default /etc/nginx/sites-available/default  
COPY ./bin/start.sh /app/start.sh  
  
EXPOSE 80  
EXPOSE 666  
EXPOSE 999  
EXPOSE 8080  
  
ENTRYPOINT ["/app/start.sh"]  
# Run app.py when the container launches  
# CMD ["bash", "start.sh"]  
# CMD service nginx start && service php5-fpm start && /bin/bash  

