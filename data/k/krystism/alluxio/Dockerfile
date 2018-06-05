FROM java:8-jre-alpine  
ENV ALLUXIO_VERSION 1.0.1  
  
RUN set -ex \  
&& apk add --no-cache --virtual .fetch-deps curl \  
&& apk add --no-cache bash openssh procps \  
&& mkdir -p /root/.ssh \  
&& ssh-keygen -t rsa -N '' -f /root/.ssh/id_rsa \  
&& chmod 600 /root/.ssh/id* \  
&& cp /root/.ssh/id_rsa /etc/ssh/ssh_host_key \  
&& cp /root/.ssh/id_rsa /etc/ssh/ssh_host_rsa_key \  
&& cp /root/.ssh/id_rsa /etc/ssh/ssh_host_ecdsa_key \  
&& cp /root/.ssh/id_rsa /etc/ssh/ssh_host_dsa_key \  
&& cp /root/.ssh/id_rsa /etc/ssh/ssh_host_ed25519_key \  
&& cat /root/.ssh/id_rsa.pub >>/root/.ssh/authorized_keys \  
&& echo "localhost" $(cat /root/.ssh/id_rsa.pub | cut -d ' ' -f 1-2)
>>/root/.ssh/known_hosts \  
&& curl -fSL
http://alluxio.org/downloads/files/${ALLUXIO_VERSION}/alluxio-${ALLUXIO_VERSION}-bin.tar.gz
-o alluxio.tar.gz \  
&& tar -xzC /usr/local -f alluxio.tar.gz \  
&& rm -rf /usr/local/alluxio-${ALLUXIO_VERSION}/build \  
&& rm -rf /usr/local/alluxio-${ALLUXIO_VERSION}/deploy \  
&& rm -rf /usr/local/alluxio-${ALLUXIO_VERSION}/tests \  
&& rm -rf /usr/local/alluxio-${ALLUXIO_VERSION}/examples \  
&& find /usr/local/alluxio-${ALLUXIO_VERSION} -name "*.java" -exec rm -f {} \;
\  
&& apk del .fetch-deps  
  
COPY docker-entrypoint.sh /usr/local/bin/  
RUN ln -s usr/local/bin/docker-entrypoint.sh / # backwards compat  
ENTRYPOINT ["docker-entrypoint.sh"]  
  
EXPOSE 22 19999  
  
CMD ["bash"]  

