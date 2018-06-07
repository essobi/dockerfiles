FROM golang:1-alpine  
  
RUN apk add --no-cache --update git openssh jq curl  
RUN mkdir -p /go/src/github.com/alexdor/github-user-interaction-fetcher  
WORKDIR /go/src/github.com/alexdor/github-user-interaction-fetcher  
RUN mkdir ~/.ssh && \  
ssh-keyscan -t rsa github.com > ~/.ssh/known_hosts  
  
# Install dep  
RUN curl -fsSL -o /usr/local/bin/dep $(curl -s
https://api.github.com/repos/golang/dep/releases/latest | jq -r ".assets[] |
select(.name | test(\"dep-linux-amd64\")) |.browser_download_url") && chmod +x
/usr/local/bin/dep  
  
# Build app  
COPY . .  
RUN dep ensure  
RUN apk del git openssh jq curl  
CMD ["go", "run", "main.go"]  
  

