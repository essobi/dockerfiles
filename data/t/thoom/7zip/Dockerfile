FROM alpine  
MAINTAINER z.d.peacock <zdp@thoomtech.com>  
  
RUN apk add --no-cache --update p7zip  
  
WORKDIR /pwd  
  
ENTRYPOINT ["/usr/bin/7za"]  
  
CMD ["--help"]  

