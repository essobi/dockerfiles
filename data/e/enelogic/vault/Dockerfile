FROM gliderlabs/alpine:3.3  
ENV VAULT_VERSION 0.5.1  
ENV VAULT_TMP /tmp/vault.zip  
ENV VAULT_HOME /usr/local/bin  
ENV PATH $PATH:${VAULT_HOME}  
  
RUN apk --no-cache add -u \  
bash \  
ca-certificates \  
python \  
py-pip \  
wget &&\  
wget --quiet --output-document=${VAULT_TMP}
https://releases.hashicorp.com/vault/${VAULT_VERSION}/vault_${VAULT_VERSION}_linux_amd64.zip
&&\  
unzip ${VAULT_TMP} -d ${VAULT_HOME} &&\  
rm -f ${VAULT_TMP} && \  
pip install supervisor supervisor-stdout  
  
ADD supervisord.conf /etc/supervisor/supervisord.conf  
ADD entrypoint.sh /  
  
RUN chmod +x /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["supervisord", "--nodaemon", "--configuration",
"/etc/supervisor/supervisord.conf"]  

