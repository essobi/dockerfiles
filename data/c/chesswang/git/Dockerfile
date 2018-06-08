FROM alpine:latest  
  
MAINTAINER WangQi chesswang197947@hotmail.com  
  
ENV LANG=en_US.UTF-8 \  
TZ=Asia/Shanghai  
  
RUN apk update \  
&& apk add openssh git tzdata \  
&& rm -rf /var/cache/apk/* /tmp/* \  
&& sed -i s/#PubkeyAuthentication.*/PubkeyAuthentication\ yes/
/etc/ssh/sshd_config \  
&& sed -i s/#PasswordAuthentication.*/PasswordAuthentication\ no/
/etc/ssh/sshd_config \  
&& sed -i s/#PermitEmptyPasswords.*/PermitEmptyPasswords\ no/
/etc/ssh/sshd_config \  
&& sed -i
s/#ChallengeResponseAuthentication.*/ChallengeResponseAuthentication\ no/
/etc/ssh/sshd_config \  
&& echo "/usr/bin/git-shell" >> /etc/shells \  
&& addgroup -g 1000 git \  
&& adduser -h /git -s /usr/bin/git-shell -G git -D -u 1000 git \  
&& passwd -d git  
  
COPY entrypoint.sh /usr/local/bin/  
  
EXPOSE 22  
VOLUME /git  
  
ENTRYPOINT ["entrypoint.sh"]  

