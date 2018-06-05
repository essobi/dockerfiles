# Builder stage.  
FROM alpine:3.6 as builder  
  
ENV REPODEST /packages  
  
# Pull in assets from context.  
ADD abuilder /usr/local/bin/  
ADD APKBUILD /home/builder/package/  
  
# Prepare the env.  
RUN apk --no-cache add alpine-sdk coreutils cmake \  
&& adduser -G abuild -g "Alpine Package Builder" -s /bin/ash -D builder \  
&& echo "builder ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers \  
&& mkdir /packages \  
&& chmod +x /usr/local/bin/abuilder \  
&& abuild -A > /carch  
  
USER builder  
WORKDIR /home/builder/package  
  
RUN /usr/local/bin/abuilder -r  
  
# Main stage.  
FROM alpine:3.6 as main  
  
LABEL maintainer="Riadh Habbachi<habbachi.riadh@gmail.com>" \  
version="1.1.3" \  
description="Borgbackup docker image based on alpine. Deduplicating \  
archiver with compression and authenticated encryption."  
  
ENV BORGBACKUP_VERSION="1.0.11-r1"  
COPY \--from=builder /carch /carch  
COPY \--from=builder /packages /packages  
COPY \--from=builder /etc/apk/keys /etc/apk/keys  
  
# Install Borg & SSH.  
RUN apk add --no-cache \  
openssh \  
sshfs \  
supervisor \  
/packages/builder/$(cat /carch)/borgbackup-1.1.3-r0.apk  
  
RUN adduser -D -u 1000 -s /bin/sh borg && \  
ssh-keygen -A && \  
mkdir /backups && \  
chown borg:borg /backups && \  
sed -i \  
-e 's/^#PasswordAuthentication yes$/PasswordAuthentication no/g' \  
-e 's/^PermitRootLogin without-password$/PermitRootLogin no/g' \  
/etc/ssh/sshd_config  
  
RUN passwd -u borg  
  
COPY supervisord.conf /etc/supervisord.conf  
  
EXPOSE 22  
CMD ["/usr/bin/supervisord"]  

