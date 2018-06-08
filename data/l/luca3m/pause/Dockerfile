FROM alpine AS build  
RUN apk add --update --no-cache alpine-sdk  
ADD pause.c /  
RUN gcc -O3 -o pause -static pause.c && strip pause  
FROM scratch  
COPY \--from=build /pause /  
ENTRYPOINT [ "/pause" ]  

