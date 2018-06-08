FROM alpine  
  
# this may not have latex support, if it does it still  
# may need texlive which is only in alpine 'edge'  
RUN apk --update add py-sphinx py-sphinx-autobuild && \  
rm -rf /var/cache/apk/*  
  
EXPOSE 8000  
WORKDIR /mnt/workdir  
  
CMD ["make", "html"]  

