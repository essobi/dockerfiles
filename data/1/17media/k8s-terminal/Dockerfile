FROM python:3.5.3-alpine  
  
ENV SHELL=/bin/sh  
  
RUN apk --no-cache add --virtual .build-deps \  
build-base \  
libffi-dev \  
openssl-dev \  
python3-dev \  
git \  
curl && \  
pip install --no-cache-dir butterfly[themes] && \  
apk --no-cache add --virtual .run-deps \  
libstdc++ \  
libffi \  
ca-certificates \  
curl \  
nano \  
busybox-suid \  
bind-tools \  
htop \  
nmap && \  
apk --no-cache add --virtual .run-deps -X http://dl-
cdn.alpinelinux.org/alpine/edge/testing \  
kubernetes && \  
apk --no-cache add --virtual .run-deps \  
zsh && \  
sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-
zsh/master/tools/install.sh)" && \  
apk del .build-deps  
COPY .zshrc /root/.zshrc  
  
VOLUME /etc/butterfly/ssl  
  
EXPOSE 8000/tcp  
  
COPY entrypoint.sh /  
RUN chmod +x /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["butterfly.server.py", "--unsecure", "--host=0.0.0.0", "--port=8000", "--
debug", "--shell=/bin/zsh"]  

