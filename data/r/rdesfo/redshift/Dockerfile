# Run redshift from a container  
#  
# docker run -it \  
# --name redshift \  
# ryan/newsbeuter  
FROM alpine:latest  
LABEL maintainer "Ryan Desfosses <ryan@desfo.org>"  
RUN apk add \--no-cache \  
redshift \  
openssl \  
ca-certificates  
  
RUN addgroup -g 1000 user \  
&& adduser -D -G user -u 1000 user  
  
USER user  
WORKDIR /home/user  
  
RUN mkdir .config \  
&& wget
"https://raw.githubusercontent.com/jonls/redshift/master/redshift.conf.sample"
-O .config/redshift.conf  
  
Entrypoint ["redshift"]  

