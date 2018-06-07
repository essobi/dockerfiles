FROM alpine as builder  
ENV version=1.14.0  
ENV download_path=/usr/local/bin/yq  
  
RUN apk add --no-cache curl  
RUN curl -L -s -o ${download_path} \  
https://github.com/mikefarah/yq/releases/download/${version}/yq_linux_amd64 \  
&& chmod +x ${download_path}  
  
FROM scratch  
COPY \--from=builder /usr/local/bin/yq /yq  
ENTRYPOINT [ "/yq" ]  

