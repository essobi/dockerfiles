FROM silintl/sshd:latest  
MAINTAINER "Phillip Shipley" <phillip_shipley@sil.org>  
  
RUN apt-get update -qq \  
&& apt-get install -y \  
curl \  
man \  
rsyslog \  
vim \  
wget  
  
RUN curl -sSL https://get.docker.com/ | sh \  
&& apt-get remove -y docker-engine  
RUN wget -O docker.deb https://apt.dockerproject.org/repo/pool/main/d/docker-
engine/docker-engine_1.7.1-0~trusty_amd64.deb \  
&& dpkg -i docker.deb  
  
COPY start-services.sh /  
COPY supervisor_sshd.conf /etc/supervisor/conf.d/  
  
CMD ["/start-services.sh"]  

