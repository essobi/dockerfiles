FROM centos:7.4.1708  
WORKDIR /usr/app  
  
RUN yum install -y unzip  
  
ENV VERSION=1.3.6.2  
RUN set -ex;\  
curl -sL
https://github.com/shawn1m/overture/releases/download/$VERSION/overture-linux-
amd64.zip -o /usr/app/overture-linux-amd64.zip;\  
unzip /usr/app/overture-linux-amd64.zip;\  
mv /usr/app/overture-linux-amd64 /usr/app/overture;\  
rm /usr/app/overture-linux-amd64.zip;  
  
EXPOSE 53  
ENTRYPOINT [ "/usr/app/overture", "-c", "/usr/app/config.json" ]

