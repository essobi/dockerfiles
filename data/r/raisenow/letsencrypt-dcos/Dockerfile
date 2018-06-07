FROM debian:jessie  
  
WORKDIR /  
RUN apt-get update && apt-get install -y unzip curl python-requests  
RUN curl -Ls -o /master.zip
https://github.com/certbot/certbot/archive/v0.5.0.zip  
RUN unzip master.zip \  
&& cd certbot-0.5.0 \  
&& ./letsencrypt-auto --help \  
&& apt-get clean && rm -rf /var/lib/apt/lists/*  
  
EXPOSE 80  
WORKDIR /certbot-0.5.0  
COPY run.sh /certbot-0.5.0/run.sh  
COPY post_cert.py /certbot-0.5.0/post_cert.py  
  
ENTRYPOINT ["/certbot-0.5.0/run.sh"]  

