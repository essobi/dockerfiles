FROM sgalkin/carnd-t2-dev:latest AS build  
  
FROM ubuntu:16.04 AS runtime  
CMD bash  
EXPOSE 4567  
RUN apt-get update && apt-get install --no-install-recommends -y \  
ca-certificates \  
libgfortran3 \  
libssl1.0.0 \  
libuv1 \  
zlib1g && \  
apt-get clean  
  
# Copy dependenices from the build image  
COPY \--from=build /usr/lib/libuWS.so /usr/lib/  
COPY \--from=build /usr/local/opt/ipopt/lib/* /usr/lib/  
  
# Preparing application directory  
RUN mkdir /app  
RUN chown nobody:nogroup /app  
USER nobody  
  
WORKDIR /app  

