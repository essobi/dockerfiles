FROM ring0club/git:2.17.1-r0  
RUN apk add openssh-keygen --no-cache  
RUN apk add gitea=1.4.1-r0 \  
\--repository https://nl.alpinelinux.org/alpine/edge/community \  
\--no-cache  
# variable USER used by gitea to check for current user(!)  
ENV GITEA_WORK_DIR=/var/lib/gitea USER=gitea  
RUN mkdir $GITEA_WORK_DIR/custom/conf && \  
cp /etc/gitea/app.ini $GITEA_WORK_DIR/custom/conf/app.ini && \  
chown -R $USER:www-data $GITEA_WORK_DIR/custom/conf  
#VOLUME $GITEA_WORK_DIR /var/log/gitea  
WORKDIR $GITEA_WORK_DIR  
USER $USER  
ENTRYPOINT ["gitea", "web"]  

