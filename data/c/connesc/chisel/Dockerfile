FROM busybox:1.27  
ENV CHISEL_VERSION 1.2.3  
RUN wget -O -
"https://github.com/jpillora/chisel/releases/download/${CHISEL_VERSION}/chisel_linux_amd64.gz"
| gunzip > /chisel \  
&& chmod +x /chisel  
  
FROM scratch  
COPY \--from=0 /chisel /chisel  
ENTRYPOINT ["/chisel"]  

