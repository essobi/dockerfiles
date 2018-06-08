FROM ubuntu:trusty  
MAINTAINER Steve de Silva <steve.desilva@gmail.com>  
  
ENV TERM=xterm-256color  
  
RUN sed -i "s/http:\/\/archive./http:\/\/uk.archive./g" /etc/apt/sources.list  
  
RUN apt-get update -qy && \  
apt-get install -qy software-properties-common && \  
apt-add-repository -y ppa:ansible/ansible && \  
apt-get update -qy && \  
apt-get install -qy ansible  
  
COPY ansible /ansible  
  
VOLUME /ansible  
WORKDIR /ansible  
  
ENTRYPOINT ["ansible-playbook"]  
CMD ["site.yml"]

