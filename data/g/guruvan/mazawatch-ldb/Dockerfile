# version 1.4-1  
# docker-version 0.9.1  
FROM busybox:buildroot-2014.02  
MAINTAINER guruvan "guruvan@maza.club"  
# We use a bootstrap script to avoid having temporary cache files and build  
# dependencies being committed and included into the docker image.  
#COPY . /tmp/  
#RUN chmod +x /tmp/bootstrap.sh && /tmp/bootstrap.sh  
VOLUME ["/home/mazachain"]  
  
ENTRYPOINT ["echo"]  
CMD ["Data-Only for Mazacoind"]  

