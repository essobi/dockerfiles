FROM alpine:edge  
LABEL maintainer="Stéphane BARON <sbaron@galilee.fr>"  
  
RUN apk add --no-cache \  
bash \  
shadow \  
python \  
py-pip \  
groff \  
less \  
&& chsh -s /bin/bash  
  
RUN pip install --upgrade awscli \  
&& rm -rf ~/.cache/pip  
  
RUN mkdir -p /root/.ssh  
COPY resources/ssh_config /root/.ssh/config  
  
COPY resources/entrypoint.sh /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]

