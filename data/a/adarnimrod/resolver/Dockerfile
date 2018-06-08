FROM cznic/knot-resolver  
RUN echo '@testing http://dl-cdn.alpinelinux.org/alpine/edge/testing' >>
/etc/apk/repositories && \  
apk add --update --no-cache \  
dma@testing \  
iproute2 \  
knot-utils \  
mailx \  
mtr  
COPY entrypoint /entrypoint  
WORKDIR /  
ENTRYPOINT [ "/entrypoint" ]  
CMD [ "bash", "--login" ]  

