FROM williamyeh/ansible:alpine3  
ENV COMPLETION_URL=https://api.github.com/repos/dysosmus/ansible-
completion/tarball  
ENV COMPLETION_DIR=/etc/bash.completion.d  
  
RUN apk add -q --no-cache \  
bash bash-completion \  
# extensions that are needed in some playbooks  
curl rsync py-netaddr  
COPY ./files/.bashrc /root/  
ENTRYPOINT [ "bash" ]  
CMD []  

