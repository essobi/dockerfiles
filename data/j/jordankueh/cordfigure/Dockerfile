FROM golang:1.9  
ENV GOPATH /go  
ENV GOBIN /go/bin  
ENV APPDIR /usr/src/app  
WORKDIR $APPDIR  
RUN go-wrapper download \  
github.com/bwmarrin/discordgo \  
gopkg.in/yaml.v2  
COPY . .  
RUN go build -o $APPDIR/cordfigure  
ENTRYPOINT $APPDIR/docker-entrypoint.sh

