FROM debian:jessie  
  
ENV HTTPTERM_VERSION HEAD  
  
ENV HTTPTERM_NAME httpterm  
ENV HTTPTERM_ARCHIVE ${HTTPTERM_NAME}-${HTTPTERM_VERSION}.tar.gz  
  
ENV HTTPTERM_MAXCONN 300000  
RUN buildDeps='curl gcc make libc-dev' && \  
apt-get update && \  
apt-get install --no-install-recommends -y ${buildDeps} && \  
  
curl -OJ
"http://git.1wt.eu/web?p=httpterm.git;a=snapshot;h=${HTTPTERM_VERSION};sf=tgz"
&& \  
  
tar zxvf ${HTTPTERM_ARCHIVE} && \  
make -C ${HTTPTERM_NAME} && \  
mv ${HTTPTERM_NAME}/httpterm /usr/local/sbin && \  
  
rm -rf /var/lib/apt/lists/* ${HTTPTERM_NAME} ${HTTPTERM_ARCHIVE} && \  
apt-get purge -y --auto-remove ${buildDeps}  
  
  
EXPOSE 8000  
ENTRYPOINT ["httpterm", "-n","${HTTPTERM_MAXCONN}",
"-N","${HTTPTERM_MAXCONN}"]  
# Intentionally use shell form here, so ^C will work.  
CMD ["-L",":8000"]  

