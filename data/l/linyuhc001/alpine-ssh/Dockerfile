FROM alpine:3.6  
LABEL maintainer="mritd <mritd1234@gmail.com>"  
  
ARG TZ="Asia/Shanghai"  
ENV TZ ${TZ}  
  
RUN apk upgrade --update \  
&& apk add bash tzdata openssh\  
&& ln -sf /usr/share/zoneinfo/${TZ} /etc/localtime \  
&& echo ${TZ} > /etc/timezone \  
&& sed -i s/#PermitRootLogin.*/PermitRootLogin\ yes/ /etc/ssh/sshd_config \  
&& ssh-keygen -t dsa -f /etc/ssh/ssh_host_dsa_key -N '' \  
&& ssh-keygen -q -t rsa -b 2048 -f /etc/ssh/ssh_host_rsa_key -N '' \  
&& ssh-keygen -q -t ecdsa -f /etc/ssh/ssh_host_ecdsa_key -N '' \  
&& ssh-keygen -t dsa -f /etc/ssh/ssh_host_ed25519_key -N '' \  
&& echo "root:root" | chpasswd \  
&& rm -rf /var/cache/apk/*  
EXPOSE 22  
CMD ["/usr/sbin/sshd", "-D"]  

