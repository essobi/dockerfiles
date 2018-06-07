FROM alpine:3.4  
MAINTAINER jakobsson.tobias@gmail.com  
  
RUN apk add --no-cache bash ruby ruby-dev ruby-rdoc ruby-irb ruby-bundler \  
ca-certificates build-base libffi libffi-dev  
  
ENTRYPOINT ["ruby"]  
CMD ["-v"]  
  

