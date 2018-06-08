FROM alpine:3.3  
RUN apk add --update alpine-sdk busybox vim zsh \  
&& adduser automation; true \  
&& addgroup automation abuild \  
&& echo "automation ALL=(ALL) ALL" >> /etc/sudoers \  
&& rm -rf /var/cache/apk/*  
USER automation  
RUN cd;git clone git://dev.alpinelinux.org/aports \  
&& git config --global user.name "Automation" \  
&& git config --global user.email "automation@someone.section.me"  

