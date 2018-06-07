  
FROM python:3.6-alpine  
# FROM alpine:edge  
MAINTAINER "Paolo D'Onorio De Meo <p.donoriodemeo@cineca.it>"  
# Note:  
# This is image is intended to be as small as possible  
RUN apk update && apk upgrade && apk add \  
bash less vim \  
curl wget git \  
jq \  
# python3 \  
&& rm -rf /var/cache/apk/*  
  
# Install pip  
RUN wget -q https://bootstrap.pypa.io/get-pip.py \  
&& python3 get-pip.py && rm *.py  
  
# Install python packages  
RUN pip --no-cache-dir install --upgrade \  
pip httpie http-prompt pyyaml  
  
# Install jqt/yq  
# https://fadado.github.io/jqt/  
RUN git clone https://github.com/fadado/jqt.git /tmp/jqt \  
&& ln -s /usr/local/bin/python /usr/bin/  
ENV PATH $PATH:/tmp/jqt/bin  
  
# Create a token from API  
ADD client_init.sh /tmp/gettoken  
  
# Handle a guest user  
ENV GUEST_SHELL /bin/bash  
ENV GUEST_USER developer  
ENV GUEST_UID 1000  
RUN adduser -s $GUEST_SHELL -u $GUEST_UID -D -h /home/$GUEST_USER $GUEST_USER  
  
# Use the new user  
USER $GUEST_USER  
ENV BASHRC /home/$GUEST_USER/.bashrc  
RUN echo "export HISTCONTROL=ignoreboth:erasedups" > $BASHRC \  
&& echo "echo -e '\\\nSet up this client with the command:'" >> $BASHRC \  
&& echo "echo -e '$ . /tmp/gettoken\\\n'" >> $BASHRC  
ENV PAGER less  
# ENV TERM=xterm  
ENV TERM=xterm-256color  

