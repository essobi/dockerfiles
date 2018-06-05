FROM alpine:edge  
  
LABEL maintainer="Paul Urban <nabru_666@hotmail.com>"  
  
ENV PACKAGES="ca-certificates ruby ruby-rake ruby-json procps curl pcre
libstdc++ libexecinfo" \  
BUILD_PACKAGES="build-base linux-headers curl-dev pcre-dev ruby-dev
libexecinfo-dev"  
RUN apk add --update $PACKAGES $BUILD_PACKAGES &&\  
gem install sinatra --no-ri --no-rdoc &&\  
mkdir -p /usr/src/app &&\  
apk del $BUILD_PACKAGES &&\  
rm -rf /var/cache/apk/* \  
/tmp/*  
ADD /src/ /usr/src/app/  
WORKDIR /usr/src/app  
RUN chown -R 1001:1001 /usr/src/app &&\  
dos2unix *.rb *.ru views/form.erb words  
USER 1001  
EXPOSE 8080  
ENTRYPOINT ["/usr/bin/ruby", "anagram.rb"]

