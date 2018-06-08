FROM rodrigomiguele/hg  
  
ENTRYPOINT []  
CMD []  
USER 0  
WORKDIR /  
  
RUN apk add meld --update-cache --repository
http://dl-3.alpinelinux.org/alpine/edge/testing/ --allow-untrusted && \  
apk info --purge  
  
USER developer  
WORKDIR /home/developer/workspace  
  
ENTRYPOINT ["hg"]  
  
CMD ["--version"]  

