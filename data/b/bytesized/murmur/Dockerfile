FROM bytesized/base  
MAINTAINER maran@bytesized-hosting.com  
  
ENV version=1.2.17  
RUN apk add --no-cache wget tar ca-certificates  
RUN wget https://github.com/mumble-
voip/mumble/releases/download/${version}/murmur-static_x86-${version}.tar.bz2  
RUN tar -xvf murmur-static_x86-${version}.tar.bz2 && \  
mv murmur-static_x86-${version} /app && \  
rm murmur-static_x86-${version}.tar.bz2  
  
VOLUME /config  
COPY static /  
  
EXPOSE 64738  

