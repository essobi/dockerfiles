FROM alpine:latest  
LABEL maintainer="sevendollar@gmail.com"  
WORKDIR /terraform  
RUN apk --updaet add --no-cache unzip curl git && \  
curl -o tf
https://releases.hashicorp.com/terraform/0.9.11/terraform_0.9.11_linux_amd64.zip?_ga=2.95965916.115305710.1501031157-510355381.1497248072
&& \  
unzip tf && \  
mv terraform /usr/local/bin/ && \  
rm tf && \  
rm -rf /var/lib/apt/lists/*  
CMD ["terraform"]  

