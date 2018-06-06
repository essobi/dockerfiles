## -*- docker-image-name: "spotify/bigtable-emulator" -*-  
FROM golang:1.7 as builder  
  
# Install netcat  
RUN apt-get update  
RUN apt-get install -y netcat  
  
# Get bigtable go package  
RUN go get -u cloud.google.com/go/bigtable  
RUN go get -d github.com/google/btree  
  
ADD bigtable-emu/bigtable-server.go /go/bin/bigtable-server.go  
RUN go build /go/bin/bigtable-server.go  
  
FROM python:3.6  
COPY \--from=builder /go /go  
COPY bigtable-emu/bigtable-server /etc/init.d/bigtable-server  
RUN chmod 700 /etc/init.d/bigtable-server  
  
RUN apt-get update  
RUN apt-get install -y ca-certificates  
  
# APP Data Req  
RUN mkdir -p /app  
WORKDIR /app  
COPY requirements.txt /app/requirements.txt  
  
# Updates  
RUN pip install --upgrade pip  
RUN pip install --no-cache-dir -r /app/requirements.txt  
RUN pip install pytest  
  
COPY . /app  
  
CMD ["bash"]

