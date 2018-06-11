FROM golang:alpine AS build-env  
LABEL maintainer "cert@rt.ru"  
LABEL repository "https://github.com/Rostelecom-CERT/vior"  
  
ENV VIOR_VERSION "0.1"  
ENV CGO_ENABLED 0  
RUN apk -U --no-cache add git \  
&& adduser -D app  
  
RUN go get github.com/Rostelecom-CERT/vior  
  
COPY cmd/vior-http/main.go /app/main.go  
  
RUN cd /app \  
&& go build -ldflags="-s -w" -a -installsuffix cgo -o /app/vior  
  
RUN chmod +x /app/vior  
  
FROM scratch  
  
COPY \--from=build-env /app/vior /vior  
COPY \--from=build-env /etc/passwd /etc/passwd  
  
USER app  
  
ENTRYPOINT ["/vior"]  

