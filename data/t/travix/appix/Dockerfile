FROM alpine:3.6  
ENV USER="appix"  
RUN apk --no-cache add curl jq busybox-suid \  
&& adduser -h /home/$USER -s /bin/sh -D -S $USER  
  
USER appix  
  
RUN touch $HOME/.profile \  
&& curl -sSL https://raw.githubusercontent.com/Travix-
International/appix/master/appixinstall.sh | sh \  
&& echo "export PATH=$PATH:$HOME/.appix" >> $HOME/.profile  
  
# source the environment  
ENTRYPOINT [ "/bin/sh", "-l" ]

