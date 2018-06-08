FROM roundcube/roundcubemail:latest  
LABEL maintainer="Mark Stillwell <mark@stillwell.me>"  
  
COPY plugins/search_defaults /usr/src/roundcubemail/plugins/search_defaults  
COPY func.inc /usr/src/roundcubemail/program/steps/mail/  
  
RUN chown -R root:root /usr/src/roundcubemail && \  
chmod -R u=rwX,g=rX,o=rX /usr/src/roundcubemail/plugins/search_defaults && \  
chmod 0644 /usr/src/roundcubemail/program/steps/mail/func.inc  

