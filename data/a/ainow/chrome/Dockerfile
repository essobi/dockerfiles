FROM alpine:3.7  
# current development of Alpine Linux  
# FROM alpine:edge  
LABEL maintainer="coolbaby"  
  
# Update apk repositories  
#RUN echo "http://dl-2.alpinelinux.org/alpine/edge/main" >
/etc/apk/repositories  
#RUN echo "http://dl-2.alpinelinux.org/alpine/edge/community" >>
/etc/apk/repositories  
#RUN echo "http://dl-2.alpinelinux.org/alpine/edge/testing" >>
/etc/apk/repositories  
# timezone  
#ARG TZ="Asia/Shanghai"  
ENV TZ Asia/Shanghai  
  
RUN apk add -U --no-cache chromium chromium-chromedriver tzdata \  
\  
#chinese fonts for alpine  
\  
&& apk add wqy-zenhei --no-cache --repository
http://nl.alpinelinux.org/alpine/edge/testing --allow-untrusted \  
&& ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime \  
&& rm -rf /var/cache/apk/* \  
/usr/share/man \  
/tmp/*  
  
COPY docker-entrypoint /usr/local/bin/  
RUN chmod +x /usr/local/bin/docker-entrypoint  
  
# Add Chrome as a user  
RUN mkdir -p /data/chrome && adduser -D chrome \  
&& chown -R chrome:chrome /data/chrome  
  
# Run Chrome non-privileged  
USER chrome  
  
# chromium port 92222,chromedriver port 9515  
EXPOSE 9222 9515  
ENTRYPOINT ["docker-entrypoint"]  
  
# chrome command line https://peter.sh/experiments/chromium-command-line-
switches/  

