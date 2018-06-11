FROM tekacs/alpine-xonsh-sshd  
  
RUN apk add alpine-sdk vim go py-virtualenv  
  
COPY boot.sh /  
  
ENTRYPOINT ["/boot.sh"]  

