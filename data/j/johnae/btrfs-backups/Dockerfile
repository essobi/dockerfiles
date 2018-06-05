FROM alpine:edge  
  
ENV SSH_PORT 22  
COPY ssh /root/.ssh  
COPY usr /usr  
COPY cmd.sh /cmd.sh  
WORKDIR /root  
  
RUN apk add -U openssh btrfs-progs coreutils bash  
  
# configure ssh  
RUN sed -i \  
-e 's/^#*\\(PermitRootLogin\\) .*/\1 yes/' \  
-e 's/^#*\\(UsePAM\\) .*/\1 no/' \  
/etc/ssh/sshd_config  
  
ENTRYPOINT ["/cmd.sh"]

