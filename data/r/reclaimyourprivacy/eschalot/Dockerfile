FROM debian:testing  
  
MAINTAINER Lars Boegild Thomsen <lth@reclaim-your-privacy.com>  
  
RUN export DEBIAN_FRONTEND=noninteractive && \  
apt-get -y update && \  
apt-get install -yq git build-essential libssl-dev openssl  
  
RUN (cd /tmp && git clone https://github.com/ReclaimYourPrivacy/eschalot.git)  
  
RUN mkdir /usr/lib/eschalot  
  
RUN (cd /tmp/eschalot && make clean && make && cp eschalot /usr/bin && cp
worgen /usr/bin && cp *.txt /usr/lib/eschalot)  
  
RUN apt-get -y remove --purge git build-essential  
RUN apt-get -y autoremove --purge  
  
RUN apt-get -y clean  
  
#RUN touch /tmp/results  
COPY eschalot.sh /  
RUN chmod +x ./eschalot.sh  
  
VOLUME ["/tmp/results"]  
  
ENTRYPOINT ["./eschalot.sh"]  
  

