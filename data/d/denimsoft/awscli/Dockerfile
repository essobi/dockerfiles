FROM alpine  
  
# install the awscli tool via pip and then discard of it  
RUN apk add --no-cache python2 groff less sudo \  
&& apk add --no-cache --virtual pip py2-pip \  
&& pip install --no-cache-dir awscli \  
&& apk del pip \  
&& echo -e "# Allow members of group wheel to execute any command\n%wheel
ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/group  
  
COPY files/docker-entrypoint.sh /usr/local/bin/docker-entrypoint.sh  
COPY files/profile.d/ /etc/profile.d/  
  
# force the default shell to be a login shell  
ENV ENV=/etc/profile  
  
# create the /conf directory to persist credentials  
RUN mkdir -p /conf \  
&& chown root:wheel /conf \  
&& chmod 0770 /conf  
  
VOLUME /conf  
  
ENTRYPOINT ["/usr/local/bin/docker-entrypoint.sh"]  
  
CMD ["--version"]  

