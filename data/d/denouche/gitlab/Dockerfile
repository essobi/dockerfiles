FROM gitlab/gitlab-ce:latest  
  
RUN echo "postfix postfix/main_mailer_type select Internet Site" | debconf-
set-selections \  
&& echo "postfix postfix/mailname string gitlab.leveugle.net" | debconf-set-
selections \  
&& apt-get install -y postfix  
  
RUN apt-get install -y \  
mailutils \  
libsasl2-2 \  
ca-certificates \  
libsasl2-modules  
  
COPY postfix-start.sh /  
RUN chmod +x postfix-start.sh  
  
RUN grep -q postfix-start.sh assets/wrapper || sed -i '/wait/i \  
/postfix-start.sh' assets/wrapper  
  
CMD ["/assets/wrapper"]  
  

