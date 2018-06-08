FROM "golang:alpine"  
  
RUN apk add \--no-cache bash curl && \  
apk add \--no-cache --virtual tmp git && \  
go get -u -d github.com/mattes/migrate/cli github.com/lib/pq && \  
go build -tags 'postgres' -o /usr/local/bin/migrate
github.com/mattes/migrate/cli && \  
apk del tmp && \  
curl https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-
it.sh > /usr/local/bin/wait-for-it && \  
chmod +x /usr/local/bin/wait-for-it  
  
ENTRYPOINT ["/bin/bash"]  

