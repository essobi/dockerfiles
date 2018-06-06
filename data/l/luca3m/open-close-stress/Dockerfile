FROM alpine AS build  
RUN apk add --update --no-cache alpine-sdk  
ADD open-close.c /  
RUN gcc open-close.c -static -o open-close  
RUN strip open-close  
FROM scratch  
STOPSIGNAL 9  
COPY \--from=build /open-close /  
ENTRYPOINT [ "/open-close" ]  

