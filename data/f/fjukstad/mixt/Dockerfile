from golang:1.7  
  
RUN go get github.com/PuerkitoBio/goquery \  
github.com/andybalholm/cascadia \  
github.com/fjukstad/gocache \  
github.com/gorilla/context \  
github.com/gorilla/mux \  
github.com/pkg/errors \  
golang.org/x/net/html \  
golang.org/x/net/html/atom  
  
RUN go get -d github.com/fjukstad/kvik/...  
  
ADD . $GOPATH/src/github.com/fjukstad/mixt/  
WORKDIR $GOPATH/src/github.com/fjukstad/mixt/  
RUN go install  
  
ENV PORT :80  
ENV COMPUTE_SERVICE compute-service:80  
  
ENTRYPOINT mixt -port=$PORT -compute-service=$COMPUTE_SERVICE  

