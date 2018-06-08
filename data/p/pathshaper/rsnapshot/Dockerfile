FROM blacklabelops/jobber  
  
# rsnapshot version (e.g. 1.4.2-r0)  
ARG RSNAPSHOT_VERSION=latest  
  
# install rsnapshot  
RUN apk upgrade --update && \  
if [ "${RSNAPSHOT_VERSION}" = "latest" ]; \  
then apk add rsnapshot ; \  
else apk add "rsnapshot=${RSNAPSHOT_VERSION}" ; \  
fi && \  
apk add \  
build-base \  
gcc \  
abuild \  
binutils \  
perl-dev \  
git && \  
export PERL_MM_USE_DEFAULT=1 && \  
perl -MCPAN -e "install Lchown" && \  
rm -rf /var/cache/apk/* && rm -rf /tmp/* && \  
mkdir -p /root/.ssh && \  
chmod 700 /root/.ssh && \  
echo "StrictHostKeyChecking no" >> /root/.ssh/config && \  
echo "UserKnownHostsFile=/dev/null" >> /root/.ssh/config && \  
mkdir -p /backup  
  
COPY docker-entrypoint.sh /root/  
  
ENTRYPOINT ["/bin/tini","--","/root/docker-entrypoint.sh"]  
CMD ["jobberd"]  

