FROM alpine:latest  
  
RUN set -xe \  
&& apk add --update build-base curl linux-pam-dev tar vsftpd \  
&& mkdir -p pam_pwdfile \  
&& cd pam_pwdfile \  
&& curl -sSL https://github.com/tiwe-de/libpam-pwdfile/archive/v1.0.tar.gz |
tar xz --strip 1 \  
&& make install \  
&& cd .. \  
&& rm -rf pam_pwdfile \  
&& apk del build-base curl linux-pam-dev tar \  
&& passwd -l root \  
&& adduser -D vsftpd \  
&& rm -rf /var/cache/apk/*  
  
RUN mkdir -p /ftp /etc/vsftpd/user_conf  
RUN chmod 777 /ftp  
COPY vsftpd.conf /etc/vsftpd/vsftpd.conf  
COPY vsftpd /etc/pam.d/vsftpd  
EXPOSE 20 21  
CMD ["vsftpd", "/etc/vsftpd/vsftpd.conf"]  

