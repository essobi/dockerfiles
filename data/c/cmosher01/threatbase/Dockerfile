FROM phusion/passenger-customizable  
  
MAINTAINER Christopher A. Mosher <cmosher01@gmail.com>  
  
RUN \  
apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get dist-upgrade -y -o Dpkg::Options::="--
force-confold" -o Dpkg::Options::="--force-confdef" \--no-install-recommends
&& \  
apt-get autoremove -y && \  
apt-get clean  
  
RUN /pd_build/python.sh  
  
RUN \  
apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y -o Dpkg::Options::="--force-
confold" -o Dpkg::Options::="--force-confdef" \--no-install-recommends \  
python-flask \  
&& \  
apt-get autoremove -y && \  
apt-get clean  
  
RUN rm -f /etc/service/nginx/down  
RUN rm /etc/nginx/sites-enabled/default  
RUN sed -i "s/worker_processes.*/worker_processes 1;/" /etc/nginx/nginx.conf  
COPY nginx.conf /etc/nginx/sites-enabled/  
  
WORKDIR /home/app  
RUN mkdir webapp  
COPY webapp/ webapp/  
RUN chown -R app: .  
WORKDIR /root  

