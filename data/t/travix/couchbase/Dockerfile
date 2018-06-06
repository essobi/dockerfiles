FROM travix/base-debian:latest  
  
MAINTAINER Travix  
  
ENV CB_VERSION=4.0.0 \  
CB_RELEASE_URL=http://packages.couchbase.com/releases \  
CB_PACKAGE=couchbase-server-community_4.0.0-ubuntu12.04_amd64.deb \  
CB_SHA256=404007eaedc3d01997eea800fcce0d0a0339bc3ab79c1c48741210f435c719f0 \  
PATH=$PATH:/opt/couchbase/bin:/opt/couchbase/bin/tools:/opt/couchbase/bin/install
\  
LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/opt/couchbase/lib \  
USER_NAME=couchbase \  
USER_ID=999 \  
GROUP_NAME=couchbase \  
GROUP_ID=999  
# Install dependencies  
RUN groupadd -r -g $GROUP_ID $GROUP_NAME \  
&& useradd -r -g $GROUP_NAME -u $USER_ID $USER_NAME \  
&& apt-get update \  
&& apt-get install -y \  
runit \  
wget \  
python-httplib2 \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \  
&& curl -fSL "$CB_RELEASE_URL/$CB_VERSION/$CB_PACKAGE" -o $CB_PACKAGE \  
&& echo "$CB_SHA256 $CB_PACKAGE" | sha256sum -c - \  
&& dpkg -i $CB_PACKAGE \  
&& rm -rf $CB_PACKAGE \  
&& mkdir -p /opt/couchbase/var/lib/couchbase \  
/opt/couchbase/var/lib/couchbase/config \  
/opt/couchbase/var/lib/couchbase/data \  
/opt/couchbase/var/lib/couchbase/stats \  
/opt/couchbase/var/lib/couchbase/logs \  
/opt/couchbase/var/lib/moxi \  
&& chown -R ${USER_NAME}:${GROUP_NAME} /opt/couchbase/var  
  
# runtime environment variables  
ENV CLUSTER_ACTION="" \  
CLUSTER_HOST_NAME="localhost" \  
CLUSTER_HOST_PORT="8091" \  
CLUSTER_RAM_SIZE="1024" \  
CLUSTER_SERVICE="data,index,query" \  
CLUSTER_ADMIN_NAME="" \  
CLUSTER_ADMIN_PASSWORD=""  
# expose ports
(http://developer.couchbase.com/documentation/server/4.1/install/install-
ports.html)  
EXPOSE 8091-8093 9100-9105 9998-9999 11207 11209-11211 11214 11215 18091-18093
4369 21100-21299  
  
CMD groupmod -g ${GROUP_ID} ${GROUP_NAME}; \  
usermod -g ${GROUP_ID} -u ${USER_ID} ${USER_NAME}; \  
chown -R ${USER_NAME}:${GROUP_NAME} /opt/couchbase/var; \  
/etc/init.d/couchbase-server start; \  
until curl -s -o /dev/null 'http://localhost:8091'; \  
do sleep 1; \  
done; \  
if [ -n "$CLUSTER_ACTION" ]; \  
echo "CLUSTER_ACTION = $CLUSTER_ACTION"; \  
then case $CLUSTER_ACTION in \  
INIT_CLUSTER) \  
echo "INIT_CLUSTER"; \  
couchbase-cli cluster-init --cluster=localhost:8091
\--user=${CLUSTER_ADMIN_NAME} --password=${CLUSTER_ADMIN_PASSWORD} --cluster-
init-ramsize=${CLUSTER_RAM_SIZE} --service=${CLUSTER_SERVICE}; \  
;; \  
ADD_TO_CLUSTER) \  
echo "ADD_TO_CLUSTER"; \  
couchbase-cli rebalance --cluster=${CLUSTER_HOST_NAME}:${CLUSTER_HOST_PORT}
--user=${CLUSTER_ADMIN_NAME} --password=${CLUSTER_ADMIN_PASSWORD} --server-
add=$(hostname):8091 \--server-add-username=${CLUSTER_ADMIN_NAME} --server-
add-password=${CLUSTER_ADMIN_PASSWORD} --service=${CLUSTER_SERVICE}; \  
;; \  
esac \  
fi; \  
ps aux; \  
/bin/su - ${USER_NAME} -c "exec tail -f
/opt/couchbase/var/lib/couchbase/logs/*"  

