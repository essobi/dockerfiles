FROM ubuntu:precise  
  
LABEL maintainer="Zadara Storage <support@zadarastorage.com>" \  
vendor="Zadara Storage"  
  
LABEL description="Advanced docker container for restoring a VPSA volume from
Object Storage"  
  
RUN apt-get update && \  
apt-get install -y ca-certificates wget libxml2 liblzo2-2 libjson0
libsqlite3-0 librtmp0 libldap-2.4-2 && \  
wget -P /tmp http://zadarastorage-public.s3.amazonaws.com/Restore_VM/curl-
z_7.35.0-03_amd64.deb http://zadarastorage-
public.s3.amazonaws.com/Restore_VM/dave-protobuf-c_0.15-10_amd64.deb
http://zadarastorage-public.s3.amazonaws.com/Restore_VM/libs3_2.0-12_amd64.deb
http://zadarastorage-public.s3.amazonaws.com/Restore_VM/zadara-
obs_15.07-1905-192.1_amd64.deb && \  
dpkg -i --force-overwrite /tmp/*.deb && \  
rm -rf /var/cache/apt/archives /var/lib/apt/lists/* /tmp/*.deb  
  
#CMD ["sleep","60m"]  
CMD ["bash","-c","zadara_obs restore --bucket=${BUCKET}
\--region=${AWS_REGION} \--access_key=${AWS_ACCESS_KEY_ID}
\--secret_key=${AWS_SECRET_ACCESS_KEY} \--snapshot=${SNAPSHOT_PATH}
\--device=${TARGET_PATH} \--end_point=${ENDPOINT}"]  

