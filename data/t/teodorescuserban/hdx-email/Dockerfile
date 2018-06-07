FROM teodorescuserban/hdx-base-email:latest  
  
MAINTAINER Serban Teodorescu, teodorescu.serban@gmail.com  
  
ENV DEBIAN_FRONTEND noninteractive  
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
RUN mkdir -p /etc/service/postfix  
ADD run_postfix /etc/service/postfix/run  
RUN chmod u+x /etc/service/postfix/run  
  
RUN mkdir -p /etc/service/opendkim  
ADD run_opendkim /etc/service/opendkim/run  
RUN chmod u+x /etc/service/opendkim/run  
  
RUN mv /etc/postfix/main.cf /etc/postfix/main.cf.orig  
ADD main.cf /etc/postfix/main.cf  
ADD aliases /etc/postfix/aliases  
RUN mv /etc/opendkim.conf /etc/opendkim.conf.orig  
ADD opendkim.conf /etc/opendkim.conf  
ADD smtp_reply_filter /etc/postfix/  
ADD trustedhosts /etc/postfix/  
ADD dkim.humdata.org.txt /etc/postfix/  
  
RUN postalias /etc/postfix/aliases  
RUN /etc/init.d/postfix start  
RUN /etc/init.d/postfix stop  
RUN chmod go-w -R /etc/postfix/  
  
RUN apt-get -qq update && apt-get -qq -y install libc-bin && apt-get clean &&
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
COPY helper_email.py /srv/  
  
EXPOSE 25  
RUN /etc/my_init.d/00_regen_ssh_host_keys.sh  
CMD ["/sbin/my_init"]  
  

