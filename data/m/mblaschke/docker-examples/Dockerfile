#############################  
# Build container (multi stage build)  
# will only be used for building  
# the application and is not part  
# of the final image  
#############################  
FROM golang as builder  
RUN mkdir /go/test  
COPY main.go /go/test  
WORKDIR /go/test  
RUN go build -o /go/test/main  
  
  
#############################  
# Final image  
#############################  
FROM scratch  
COPY --from=builder /go/test/main /  
CMD ["/main"]  

