FROM alpine:edge  
MAINTAINER Martin Venuš "martin.venus@gmail.com"  
ENV PATH="/root/.yarn/bin:${PATH}"  
RUN apk --update add bash curl git gnupg nodejs && \  
curl -o- -L https://yarnpkg.com/install.sh | bash && \  
mkdir -p /app  
  
WORKDIR "/app"  
VOLUME ["/app"]  
  
CMD ["yarn"]  

