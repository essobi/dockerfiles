FROM alpine:latest  
RUN apk add --update netcat-openbsd bash wget tar xz && rm -rf
/var/cache/apk/*  
COPY ./nyc_collision_data.csv.xz /data/nyc_collision_data.csv.xz  
COPY ./build.sh /data/build.sh  
CMD ["nc"]  

