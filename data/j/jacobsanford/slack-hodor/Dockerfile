FROM frolvlad/alpine-glibc  
MAINTAINER Jacob Sanford <jsanford_at_unb.ca>  
  
ENV SLACK_TOKEN NULL  
ENV RTMBOT_VERSION 0.3.0  
RUN apk add --update \  
python \  
py-pip \  
openssl && \  
pip install websocket-client>=0.44.0 && \  
rm -rf /var/cache/apk/*  
  
WORKDIR /app  
RUN wget -O rtmbot.zip https://github.com/slackhq/python-
rtmbot/archive/$RTMBOT_VERSION.zip && \  
unzip rtmbot.zip && rm rtmbot.zip && \  
ls && \  
mv python-rtmbot-$RTMBOT_VERSION/* . && mv docs/example-config/rtmbot.conf .
&& \  
wget -O hodor.zip https://github.com/JacobSanford/python-rtmbot-
hodor/archive/master.zip && \  
unzip hodor.zip && rm hodor.zip && \  
mv python-rtmbot-hodor-master plugins/python-rtmbot-hodor && \  
pip install -r /app/requirements.txt  
  
COPY bin/hodor.sh /app/hodor.sh  
  
ENTRYPOINT ["/app/hodor.sh"]  

