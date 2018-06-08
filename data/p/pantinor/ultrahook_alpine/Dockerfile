FROM alpine:3.6  
WORKDIR /tmp  
RUN apk add --no-cache ruby ruby-dev ruby-json  
ADD src /tmp  
RUN gem build -v ultrahook \  
&& gem install --no-document net-http-persistent \  
&& gem install --no-document --local ultrahook  
ADD ./ultrahook.sh /usr/bin/  
RUN rm -rf src  
RUN apk del ruby-dev \  
&& rm -rf /var/cache/apk/*  
ENTRYPOINT "/usr/bin/ultrahook.sh"

