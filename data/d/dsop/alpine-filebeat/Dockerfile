FROM dsop/alpine-base  
  
ENV GLIBC 2.23-r3  
ENV FILEBEAT_VERSION 1.3.1-x86_64  
ENV USER_ID 1000  
ENV USER_NAME filebeat  
  
RUN curl -L https://raw.githubusercontent.com/sgerrand/alpine-pkg-
glibc/master/sgerrand.rsa.pub -o /etc/apk/keys/sgerrand.rsa.pub && \  
curl -L https://github.com/sgerrand/alpine-pkg-
glibc/releases/download/${GLIBC}/glibc-${GLIBC}.apk -o glibc-${GLIBC}.apk && \  
apk add glibc-${GLIBC}.apk && \  
rm glibc-${GLIBC}.apk  
  
RUN mkdir /opt && \  
cd /opt && \  
curl -L
https://download.elastic.co/beats/filebeat/filebeat-${FILEBEAT_VERSION}.tar.gz
-o filebeat-${FILEBEAT_VERSION}.tar.gz && \  
tar xzf filebeat-${FILEBEAT_VERSION}.tar.gz && \  
ln -s filebeat-${FILEBEAT_VERSION} filebeat && \  
ln -s /opt/filebeat/filebeat /usr/local/bin/  
  
RUN adduser -u ${USER_ID} -D ${USER_NAME} -s /bin/bash  
RUN cp /root/.bashrc /home/${USER_NAME} && \  
chown -R ${USER_ID}:${USER_ID} /home/${USER_NAME}  
  
USER ${USER_NAME}  
WORKDIR /home/${USER_NAME}  
  
ENTRYPOINT ["filebeat"]  

