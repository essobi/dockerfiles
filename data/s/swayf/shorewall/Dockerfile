  
# shorewall in a container  
#  
# docker run --rm -it \  
# -v /etc/shorewall:/etc/shorewall  
# --net host \  
# --cap-add NET_ADMIN \  
# --privileged \  
# user/shorewall  
#  
FROM debian:stretch  
  
MAINTAINER oleg butovich <obutovich@gmail.com>  
  
RUN apt-get update  
RUN apt-get upgrade -y  
RUN apt-get install shorewall -y  
  
ENTRYPOINT [ "/sbin/shorewall" ]

