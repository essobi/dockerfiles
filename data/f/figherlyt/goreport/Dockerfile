From golang:1.9.1-stretch  
RUN apt-get update && apt-get install -y graphviz  
RUN go get -u github.com/fighterlyt/goreporter  
WORKDIR /go/src/github.com/fighterlyt/goreporter  
RUN go-wrapper download  
RUN go-wrapper install  
RUN ["go", "build", "main.go"]  
RUN mv main /go/report  
ENV format html #默认的输出格式  
ENV path ""  
ENV except ""  
VOLUME ["/go/src"]  
VOLUME ["/go/output"]  
WORKDIR /go/src  
ENTRYPOINT ../report -p $path -e $except -r /go/output  

