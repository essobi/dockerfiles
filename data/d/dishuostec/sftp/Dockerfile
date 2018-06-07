FROM alpine:3.7  
LABEL maintainer="dishuostec <dishuostec@gmail.com>"  
  
ARG ALPINE_REPO=http://dl-cdn.alpinelinux.org  
  
ENV PASS=xxxxxxxx  
  
RUN ver=$(cat /etc/alpine-release | awk -F '.' '{printf "%s.%s", $1, $2;}') \  
&& repos=/etc/apk/repositories \  
&& mv -f ${repos} ${repos}_bk \  
&& echo "${ALPINE_REPO}/alpine/v${ver}/main" > ${repos} \  
&& echo "${ALPINE_REPO}/alpine/v${ver}/community" >> ${repos} \  
&& apk add --no-cache tzdata \  
&& ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime \  
&& echo Asia/Shanghai > /etc/timezone \  
\  
&& apk add --no-cache openssh \  
&& ssh-keygen -A \  
&& mkdir /sftp \  
&& chown root:root /sftp \  
&& chmod 755 /sftp \  
# 1000 is the uid/gid for "node" in official image  
&& addgroup -g 1000 -S node \  
&& adduser -u 1000 -h /sftp/app -s /sbin/nologin -D -G node node \  
\  
&& sed -i 's/^Subsystem/#Subsystem/' /etc/ssh/sshd_config \  
&& sed -i '/^#Subsystem/ i Subsystem sftp internal-sftp' /etc/ssh/sshd_config
\  
&& sed -i '/^#Subsystem/ i Match User node' /etc/ssh/sshd_config \  
&& sed -i '/^#Subsystem/ i \ ChrootDirectory /sftp' /etc/ssh/sshd_config \  
&& sed -i '/^#Subsystem/ i \ AllowTcpForwarding no' /etc/ssh/sshd_config \  
&& sed -i '/^#Subsystem/ i \ X11Forwarding no' /etc/ssh/sshd_config \  
&& sed -i '/^#Subsystem/ i \ ForceCommand internal-sftp' /etc/ssh/sshd_config  
  
EXPOSE 22  
CMD ["ash", "-c", "echo -e node:${PASS} | chpasswd; /usr/sbin/sshd -D -E
/dev/stderr"]  

