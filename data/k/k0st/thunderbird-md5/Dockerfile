FROM k0st/ubuntu-old:natty  
MAINTAINER kost - https://github.com/kost  
  
ADD root/ /  
RUN apt-get autoclean && apt-get autoremove && apt-get update && \  
apt-get -qqy install --no-install-recommends enigmail thunderbird gnupg
libcanberra-gtk-module && \  
rm -rf /var/lib/apt/lists/* && \  
adduser --uid 1000 --system user && \  
echo "Success"  
  
VOLUME ["/home/user"]  
  
USER user  
WORKDIR /home/user  
  
ENTRYPOINT ["thunderbird","--no-remote"]  

