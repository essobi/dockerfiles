FROM 2chat/ubuntu:xenial  
LABEL maintainer="roma.gordeev@gmail.com"  
  
EXPOSE 8888  
EXPOSE 20000-65535/udp  
EXPOSE 8433  
EXPOSE 3478  
# install kurento media server  
RUN echo "deb http://ubuntu.kurento.org/ xenial kms6" | tee
/etc/apt/sources.list.d/kurento.list \  
&& wget -O - http://ubuntu.kurento.org/kurento.gpg.key | apt-key add - \  
&& apt-get update \  
&& apt-get -y install kurento-media-server-6.0 \  
&& apt-get -y install kms-pointerdetector-6.0 \  
&& apt-get -y install gnutls-bin \  
&& apt-get -y install openh264-gst-plugins-bad-1.5 \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
# generate self-signed key  
RUN certtool --generate-privkey --outfile /etc/kurento/defaultCertificate.pem
\  
&& echo 'organization = your organization name' > /etc/kurento/certtool.tmpl \  
&& certtool --generate-self-signed --load-privkey
/etc/kurento/defaultCertificate.pem --template /etc/kurento/certtool.tmpl >>
/etc/kurento/defaultCertificate.pem \  
&& chown kurento /etc/kurento/defaultCertificate.pem  
  
WORKDIR /  
  
# set up kurento config file  
COPY kurento.conf.json /etc/kurento/kurento.conf.json  
# set up docker entrypoint script  
COPY entrypoint.sh /entrypoint.sh  
RUN chmod +x /entrypoint.sh  
  
# set up gstreamer logging level to 5 (log everything) for Kurento process  
ENV GST_DEBUG=Kurento*:5  
ENTRYPOINT ["/entrypoint.sh"]  

