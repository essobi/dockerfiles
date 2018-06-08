FROM golang:1.10 as builder  
  
ENV IMPORTPATH=github.com/sensebox/sensebox-mailer  
  
WORKDIR /go/src/${IMPORTPATH}  
  
COPY . ./  
  
# Compile static assets  
RUN go get github.com/rakyll/statik && \  
statik -src=/go/src/${IMPORTPATH}/templates  
  
RUN export branch=$(git rev-parse --abbrev-ref HEAD) && \  
export ts=$(TZ=UTC git log \--date=local \--pretty=format:"%ct" -n 1) && \  
export hash=$(TZ=UTC git log \--date=local \--pretty=format:"%h" -n 1) && \  
CGO_ENABLED=0 go install -a -tags netgo -ldflags "-extldflags -static -X
main.branch=$branch -X main.ts=$ts -X main.hash=$hash"
${IMPORTPATH}/cmd/sensebox-mailer  
  
FROM scratch  
  
COPY \--from=builder /etc/ssl/certs/ /etc/ssl/certs  
  
COPY \--from=builder /go/bin/sensebox-mailer /sensebox-mailer  
  
CMD ["/sensebox-mailer"]  

