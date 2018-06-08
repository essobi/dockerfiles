FROM nephatrine/base-alpine:latest  
LABEL maintainer="Daniel Wolf <nephatrine@gmail.com>"  
  
RUN echo "====== RUNTIME CONFIGURATION ======" \  
&& apk --update upgrade \  
&& apk add \  
git \  
openssh-keygen \  
openssh-server \  
sqlite \  
&& mkdir -p /mnt/data \  
\  
&& echo "====== CONFIGURE USER ======" \  
&& usermod -p '*' -s /bin/bash guardian \  
\  
&& echo "====== INSTALL GITEA ======" \  
&& cd /usr/local/bin \  
&& wget -O gitea.xz https://dl.gitea.io/gitea/master/gitea-master-linux-
amd64.xz \  
&& unxz gitea.xz && chmod +x gitea \  
\  
&& echo "====== CLEANUP ======" \  
&& cd /usr/src \  
&& rm -rf \  
/tmp/* \  
/usr/src/* \  
/var/cache/apk/*  
  
EXPOSE 22/tcp 3000/tcp  
COPY override /  

