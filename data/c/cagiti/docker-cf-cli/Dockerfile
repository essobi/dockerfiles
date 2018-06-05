FROM alpine:3.5  
MAINTAINER Cai Cooper "caicooper82@gmail.com"  
ARG CF_CLI_VERSION="6.26.0"  
RUN apk add --no-cache --update unzip curl openssl ca-certificates git ruby
ruby-json libc6-compat \  
&& ln -s /lib/ /lib64  
  
RUN curl -L
"https://cli.run.pivotal.io/stable?release=linux64-binary&version=${CF_CLI_VERSION}"
| tar -zx -C /usr/local/bin  
  
ENTRYPOINT ["cf"]  

