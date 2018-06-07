FROM alpine  
  
ENV KERNEL_VERSION=4.9.45-rancher EXTRA_VERSION=4.9.45-nvidia-375.66-2  
LABEL maintainer="Alexandre Buisine <alexandrejabuisine@gmail.com>"
version="$EXTRA_VERSION"  
  
RUN apk add --no-cache bash  
  
COPY resources/extra.sh /usr/local/bin/extra.sh  
COPY resources/extras-${EXTRA_VERSION}.tar.gz /  
  
RUN chmod +x /usr/local/bin/extra.sh  
  
CMD [ "extra.sh" ]

