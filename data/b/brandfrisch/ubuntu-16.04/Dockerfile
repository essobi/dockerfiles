# docker build -t brandfrisch-ubuntu-16.04/latest .  
# docker run -it --privileged --rm=true -v $(pwd):/mnt/host brandfrisch-
ubuntu-16.04/latest  
FROM ubuntu:16.04  
# set env vars  
ENV container docker  
ENV LC_ALL C  
ENV DEBIAN_FRONTEND noninteractive  
  
# configure apt behaviour  
RUN echo "APT::Get::Install-Recommends 'false'; \n\  
APT::Get::Install-Suggests 'false'; \n\  
APT::Get::Assume-Yes "true"; \n\  
APT::Get::force-yes "true";" > /etc/apt/apt.conf.d/00-general  
  
# systemd tweaks  
RUN rm -rf /lib/systemd/system/getty*;  
  
# install  
RUN apt-get update && apt-get upgrade -qy && apt-get dist-upgrade -qy && apt-
get install -yq apt-utils  
  
# install typical requirements for testing  
RUN apt-get install -y procps ssl-cert ca-certificates apt-transport-https
python python-pip sudo curl net-tools vim iproute unzip vim wget git  
  
# install virtualenv  
RUN pip install virtualenv  
  
# install goss  
RUN curl -L https://github.com/aelsabbahy/goss/releases/download/v0.3.5/goss-
linux-amd64 -o /usr/local/bin/goss  
RUN chmod +rx /usr/local/bin/goss  
  
# ansible-lint-rules  
COPY ansible-lint-rules /usr/local/src/ansible-lint-rules  
  
# cleanup  
RUN apt-get clean  
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# finally run script on startup  
CMD ["/bin/bash"]

