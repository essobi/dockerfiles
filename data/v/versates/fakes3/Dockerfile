FROM alpine:3.4  
MAINTAINER Versates <docker@versates.com>  
  
ENV LANG "en_US.UTF8"  
RUN addgroup -S fakes3 && adduser -h /var/lib/fakes3 -D -S -G fakes3 fakes3 \  
&& mkdir -p /var/run/fakes3 && chown fakes3:fakes3 /var/run/fakes3 \  
&& apk add --update --no-cache \  
su-exec \  
ca-certificates \  
ruby \  
ruby-rdoc \  
ruby-irb \  
ruby-bundler \  
&& gem install fakes3 \  
&& rm -rf /var/cache/apk/*  
  
WORKDIR "/var/lib/fakes3"  
VOLUME "/var/lib/fakes3"  
  
EXPOSE 4569  
COPY entrypoint /usr/local/bin/  
ENTRYPOINT ["entrypoint"]  
CMD ["fakes3", "-r", "/var/lib/fakes3", "-p", "4569"]  

