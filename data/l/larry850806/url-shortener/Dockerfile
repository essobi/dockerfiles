FROM larry850806/golang-workspace AS build  
  
COPY src/main /root/workspace/src/main  
  
WORKDIR /root/workspace/src/main  
  
# install dependencies and build  
RUN dep ensure && go build  
  
FROM gcr.io/distroless/base  
  
WORKDIR /app  
  
COPY \--from=build /root/workspace/src/main/main /app/main  
  
CMD ["./main"]

