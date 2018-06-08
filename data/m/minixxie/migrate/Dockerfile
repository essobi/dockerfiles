FROM golang:1.9.2 as build  
RUN \  
go get -u -d github.com/mattes/migrate/cli \  
github.com/kshvakov/clickhouse \  
github.com/cockroachdb/cockroach-go/crdb \  
github.com/gocql/gocql \  
github.com/go-sql-driver/mysql \  
github.com/lib/pq \  
github.com/cznic/ql/driver \  
cloud.google.com/go/spanner github.com/googleapis/gax-go \  
github.com/mattn/go-sqlite3  
RUN \  
go build \  
-tags "cassandra clickhouse cockroachdb crate mongodb mysql neo4j postgres ql redshift shell spanner sqlite3" \  
-o /usr/local/bin/migrate github.com/mattes/migrate/cli  
  
FROM gcr.io/distroless/base  
COPY --from=build /usr/local/bin/migrate /  
VOLUME /migrations  
ENTRYPOINT ["/migrate"]  

