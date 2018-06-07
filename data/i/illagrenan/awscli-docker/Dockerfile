FROM docker:latest  
LABEL authors="Vašek Dohnal <vaclav.dohnal@gmail.com>"  
RUN apk add --purge --no-cache --update python3  
RUN pip3 install --ignore-installed --isolated --no-input --compile --exists-
action=a --disable-pip-version-check --use-wheel --no-cache-dir awscli  

