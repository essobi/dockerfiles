# NOTE: Track bug resolution  
FROM jacobsvante/python:3.7.0a3-alpine3.6-with-bpo-31940-lchown-fix  
  
ARG user=service  
ARG envname=py3  
  
RUN apk update  
RUN apk add -t build-deps libffi-dev build-base && \  
apk del build-deps && rm -rf /var/cache/apk/*  
  
RUN umask 775  
RUN adduser -h /home/$user -D -g "" -s /bin/bash $user  
  
USER $user  
WORKDIR /home/$user  
  
RUN python3 -m venv /home/$user/$envname  
RUN /home/$user/$envname/bin/pip install --upgrade pip  
  
COPY . /home/$user/  
  
RUN /home/$user/$envname/bin/pip install .  
  
EXPOSE 8080  
ENTRYPOINT ["/home/service/py3/bin/carmen-web"]  

