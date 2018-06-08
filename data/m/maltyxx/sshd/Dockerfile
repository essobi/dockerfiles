FROM debian:jessie  
  
LABEL maintainer="Yoann VANITOU <yvanitou@gmail.com>"  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && \  
apt-get --yes install openssh-server rsync && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
RUN mkdir -vp /var/run/sshd  
RUN mkdir -vp /usr/local/etc/sshd  
  
COPY ./sshd/* /usr/local/etc/sshd/  
COPY ./entrypoint.sh /  
  
RUN chmod -v 644 /usr/local/etc/sshd/*  
RUN chmod -v 755 /entrypoint.sh  
  
VOLUME /usr/local/etc/sshd  
  
EXPOSE 22  
ENTRYPOINT ["/entrypoint.sh"]

