FROM golang  
  
USER nobody  
  
ENV HOME=/tmp  
ENV HTTP_PORT=8080  
ENV DB_FILENAME=$HOME/db/electronicArtArgentina.sqlite3  
ENV GIN_MODE=release  
  
#ENV TMPL_DIR=$HOME/tmpl  
#COPY ["tmpl/index.tmpl", "$TMPL_DIR/index.tmpl"]  
COPY ["certs/ca-certificates.crt", "/etc/ssl/certs/ca-certificates.crt"]  
COPY ["db/electronicArtArgentina.sqlite3", "$DB_FILENAME"]  
COPY ["api.go", "$HOME/api.go"]  
COPY ["events.go", "$HOME/events.go"]  
COPY ["exhibitions.go", "$HOME/exhibitions.go"]  
COPY ["locations.go", "$HOME/locations.go"]  
COPY ["search.go", "$HOME/search.go"]  
COPY ["techniques.go", "$HOME/techniques.go"]  
  
WORKDIR $HOME  
  
RUN chown $USER:$USER $HOME -R \  
&& go get github.com/coopernurse/gorp \  
&& go get github.com/mattn/go-sqlite3 \  
&& go get github.com/aviddiviner/gin-limit \  
&& go get github.com/gin-gonic/gin \  
&& go build -o $HOME/api-arte-electronico *.go  
  
EXPOSE 8080  
ENTRYPOINT ["/tmp/api-arte-electronico"]  

