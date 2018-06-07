FROM golang  
  
RUN go get -u -v github.com/bitly/go-nsq  
  
COPY ./ /project  
  
ENTRYPOINT ["/project/start.sh"]

