#  
# docker run -ti --rm \  
# -v /tmp/mpd:/tmp/mpd \  
# --network host \  
# germangb/ncmpcpp  
#  
FROM ubuntu:trusty  
MAINTAINER germangb <germangb42@gmail.com>  
  
RUN apt-get update \  
&& apt-get install -y ncmpcpp \  
$$ rm -rf /var/lib/apt/lists/*  
  
COPY config /root/.config/ncmpcpp/config  
  
ENTRYPOINT ["ncmpcpp"]  

