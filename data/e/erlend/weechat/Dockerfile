FROM alpine  
  
RUN apk add -U weechat su-exec tini py2-pip python-dev alpine-sdk && \  
pip install --upgrade python-potr && \  
apk del python-dev alpine-sdk && \  
rm -rf /var/cache/apk/*  
  
RUN adduser -D weechat  
  
ENV LANG=C.UTF-8 WEECHAT_HOME=/config  
  
EXPOSE 9001  
VOLUME /config  
  
COPY entrypoint.sh /  
ENTRYPOINT ["/entrypoint.sh"]  

