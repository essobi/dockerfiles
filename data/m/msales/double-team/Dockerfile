# Build container  
FROM golang:1.10 as builder  
  
RUN curl https://raw.githubusercontent.com/golang/dep/master/install.sh | sh  
  
WORKDIR /go/src/github.com/msales/double-team/  
COPY ./ .  
RUN dep ensure  
  
RUN CGO_ENABLED=0 GOOS=linux go build -a -ldflags '-s' -o double-team
./cmd/double-team  
  
# Run container  
FROM scratch  
  
COPY \--from=builder /go/src/github.com/msales/double-team/double-team .  
  
ENV DOUBLE_TEAM_PORT "80"  
EXPOSE 80  
CMD ["./double-team", "server"]

