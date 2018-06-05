FROM instrumentisto/glide:latest  
  
WORKDIR /go/src/github.com/GallenHu/bookmarkgo/  
  
ADD . /go/src/github.com/GallenHu/bookmarkgo/  
  
RUN glide install && touch /go/app.ini && go build -o main .  
  
EXPOSE 3001  
# must be ENTRYPOINT  
# docker run -v /your/temp/app.ini:/go/app.ini -p 3001:3001 bookmark:v1  
ENTRYPOINT ["./main", "-c", "/go/app.ini"]

