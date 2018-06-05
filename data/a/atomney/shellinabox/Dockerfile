FROM ubuntu:xenial  
RUN apt update && \  
apt install -y shellinabox openssl ssh  
EXPOSE 4200  
CMD ["shellinaboxd", "--no-beep", "--port=4200", "--
cert=/var/lib/shellinabox", "--user=shellinabox", "--
service=/:SSH:172.17.0.1", "--css", "/etc/shellinabox/options-
available/00_White On Black.css"]  

