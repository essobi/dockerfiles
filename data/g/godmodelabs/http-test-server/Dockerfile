FROM gliderlabs/alpine:latest  
MAINTAINER Daniel Poßmann <daniel.possmann@boerse-go.de>  
  
RUN apk add --update ruby ca-certificates && \  
rm -rf /var/cache/apk/* && \  
gem install -N sinatra  
  
EXPOSE 4567  
ADD . /  
  
ENTRYPOINT ["ruby"]  
CMD ["/server.rb", "-o","0.0.0.0"]

