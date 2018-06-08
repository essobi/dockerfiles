FROM centos:centos7  
  
RUN \  
( \  
echo "[kubernetes]" && \  
echo "name=Kubernetes" && \  
echo "baseurl=https://packages.cloud.google.com/yum/repos/kubernetes-
el7-x86_64" && \  
echo "enabled=1" && \  
echo "gpgcheck=1" && \  
echo "repo_gpgcheck=1" && \  
echo "gpgkey=https://packages.cloud.google.com/yum/doc/yum-key.gpg
https://packages.cloud.google.com/yum/doc/rpm-package-key.gpg" \  
) | \  
cat > /etc/yum.repos.d/kubernetes.repo && \  
yum clean all && \  
yum upgrade -y && \  
yum install -y epel-release && \  
yum install -y docker kubelet kubeadm kubectl bind-libs-lite systemd-sysv jq
&& \  
yum list installed | awk 'NR >2 {print $1}' >/tmp/installed.pkg && \  
curl -L "https://packages.cloud.google.com/yum/doc/yum-key.gpg" -o yum-key.gpg
&& \  
curl -L "https://packages.cloud.google.com/yum/doc/rpm-package-key.gpg" -o
rpm-package-key.gpg && \  
mkdir /data && \  
cd /data && \  
cat /tmp/installed.pkg | while read line; do \  
yumdownloader $line; \  
done && \  
yum install -y createrepo && \  
createrepo .  
  
FROM nginx:alpine  
COPY --from=0 /data /data  
RUN echo "server {autoindex off; server_name localhost; location ~ ^/$ {return
200;} location ~ ^.*/$ {return 404;} location / { root /data; default_type
application/octet-stream; add_header Content-Disposition 'attachment'; types
{}}}" > /etc/nginx/conf.d/default.conf  

