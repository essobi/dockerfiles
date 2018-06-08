FROM golang:alpine  
  
RUN apk add --no-cache --virtual git  
  
# Install migrate for db migrations  
RUN go get -u -d github.com/mattes/migrate/cli github.com/lib/pq && \  
go build -tags 'postgres' -o /usr/local/bin/migrate
github.com/mattes/migrate/cli  
  
ENTRYPOINT ["migrate"]  
CMD ["--help"]  

