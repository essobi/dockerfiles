FROM geertbongers/ubuntu-dockerize  
MAINTAINER Geert  
  
RUN apt-get update && apt-get install -qy --force-yes git-core python
libjpeg8-dev libpng-dev libfreetype6-dev zlib1g-dev libopenjpeg-dev libwebp-
dev python-pip &&\  
apt-get install -qy python-imaging python-psutil python-pil  
RUN git clone https://github.com/Hellowlol/HTPC-Manager /htpc-manager &&\  
cd /htpc-manager && git checkout master2  
  
EXPOSE 8085  
VOLUME /container-data  
  
CMD ["--datadir", "/container-data"]  
ENTRYPOINT ["dockerize", "-stdout", "/container-data/htpcmanager.log",
"python", "/htpc-manager/Htpc.py"]

