FROM frolvlad/alpine-python3:latest  
MAINTAINER Facundo Bianco <vando@van.do>  
  
RUN apk add --no-cache ca-certificates openssl  
RUN pip3 install hangups  
  
ADD https://github.com/mtomwing/pickups/archive/master.tar.gz
/usr/local/src/pickups.tgz  
RUN tar -C /usr/local/src -zxf /usr/local/src/pickups.tgz  
RUN mv /usr/local/src/pickups-master/pickups /usr/lib/python3.5/  
RUN rm -r /usr/local/src/pickups*  
  
RUN adduser -h /home -s /bin/false -D pickups  
USER pickups  
RUN mkdir -p /home/pickups/.cache/hangups /home/pickups/.config/hangups  
  
EXPOSE 6667  
VOLUME ["/home/pickups/.config/hangups", "/home/pickups/.cache/hangups"]  
CMD ["/usr/bin/python3.5", "-m", "pickups", "--address", "0.0.0.0"]  

