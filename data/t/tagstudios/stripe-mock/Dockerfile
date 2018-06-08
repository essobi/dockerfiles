FROM golang:1.9-alpine  
  
RUN apk add --update --no-cache git  
  
RUN go get -v -u github.com/stripe/stripe-mock  
  
EXPOSE 12111  
ENTRYPOINT ["stripe-mock"]  

