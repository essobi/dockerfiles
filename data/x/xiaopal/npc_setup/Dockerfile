FROM alpine:3.7  
# ARG ALPINE_MIRROR=http://mirrors.aliyun.com/alpine  
# echo -e "$ALPINE_MIRROR/v3.6/main\n$ALPINE_MIRROR/v3.6/community"
>/etc/apk/repositories  
ARG NPC_DL_MIRROR=http://npc.nos-eastchina1.126.net/dl  
RUN apk add --no-cache bash curl openssh-client openssl git ansible nginx
findutils py-netaddr \  
&& curl "$NPC_DL_MIRROR/dumb-init_1.2.0_amd64.tar.gz" | tar -zx -C /usr/bin \  
&& mkdir -p ~/.ssh && chmod 700 ~/.ssh \  
&& echo -e 'StrictHostKeyChecking no\nUserKnownHostsFile /dev/null'
>~/.ssh/config \  
&& ansible-galaxy install -p /etc/ansible/roles xiaopal.npc_setup \  
&& ansible-playbook /etc/ansible/roles/xiaopal.npc_setup/tests/noop.yml  
  
ADD run.sh /  
RUN chmod a+x /run.sh  
  
EXPOSE 80  
CMD ["/run.sh"]  
  

