FROM alpine:3.7  
RUN apk add --update --no-cache \  
ruby \  
ruby-dev \  
ruby-ffi \  
&& \  
gem install --no-document sass  
  
WORKDIR /app  
  
CMD ["sass"]

