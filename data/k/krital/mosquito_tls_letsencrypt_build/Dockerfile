FROM ansi/mosquitto  
  
MAINTAINER Alex Kritikos <alex@kritikal.org>  
  
  
  
USER root  
  
RUN sudo apt-get update  
RUN sudo apt-get upgrade -y  
RUN apt-get install openssl git augeas-lenses dialog libaugeas0 libexpat1-dev
libffi-dev libpython-dev libpython2.7 libpython2.7-dev python-dev python-pkg-
resources python-setuptools python-virtualenv python2.7-dev -y  
RUN echo 'root:Mosquitto!' | chpasswd  
  
RUN mkdir -p /etc/mosquitto  
WORKDIR /etc/mosquitto  
#RUN chown -R mosquitto /etc/mosquitto  
#RUN wget https://letsencrypt.org/certs/isrgrootx1.pem  
#USER mosquitto  
RUN git clone https://github.com/certbot/certbot  
WORKDIR /etc/mosquitto/certbot  
#USER root  
#RUN ./certbot-auto certonly --standalone -n -v --agree-tos --email
root@example.com -d example.com -d www.example.com --config-dir /etc/mosquitto
--work-dir /etc/mosquitto --logs-dir /etc/mosquitto  
RUN ./letsencrypt-auto --email alex@kritikal.org --text --authenticator manual
--work-dir /etc/mosquitto --config-dir /etc/mosquitto --logs-dir
/etc/mosquitto auth --cert-path /etc/mosquitto/certs/ --chain-path
/etc/mosquitto/chains/ --csr ~/Desktop/domain.csr  
  
USER mosquitto  
RUN printenv  

