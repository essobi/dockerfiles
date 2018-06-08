FROM ring0club/git:2.17.1-r0  
RUN apk add openssh-keygen --no-cache  
RUN apk add gogs=0.11.34-r0 \  
\--repository https://nl.alpinelinux.org/alpine/edge/community \  
\--no-cache  
# variable USER used by gogs to check for current user(!)  
ENV GOGS_CUSTOM=/var/lib/gogs USER=gogs  
RUN mkdir $GOGS_CUSTOM/conf && \  
cp /etc/gogs/conf/app.ini $GOGS_CUSTOM/conf/app.ini && \  
chown -R $USER:www-data $GOGS_CUSTOM/conf  
#VOLUME $GOGS_CUSTOM /var/log/gogs  
WORKDIR $GOGS_CUSTOM  
USER $USER  
ENTRYPOINT ["gogs", "web"]  

