FROM alpine  
  
MAINTAINER RekGRpth  
  
ADD entrypoint.sh /  
  
ENV HOME=/data \  
LANG=ru_RU.UTF-8 \  
TZ=Asia/Yekaterinburg \  
USER=apache \  
GROUP=apache  
  
RUN apk add --no-cache \  
alpine-sdk \  
apache2 \  
apache2-ldap \  
apache2-ssl \  
coreutils \  
perl \  
perl-cgi \  
perl-cgi-session \  
perl-dbd-pg \  
perl-dbi \  
perl-utils \  
perl-yaml-syck \  
shadow \  
su-exec \  
tzdata \  
&& cpan -i CGI/Deurl.pm \  
&& apk del \  
alpine-sdk \  
perl-utils \  
&& chmod +x /entrypoint.sh \  
&& usermod --home "${HOME}" "${USER}" \  
&& mkdir -p /run/apache2  
  
VOLUME ${HOME}  
  
WORKDIR ${HOME}/app  
  
ENTRYPOINT ["/entrypoint.sh"]  
  
CMD [ "httpd", "-D", "FOREGROUND" ]  

