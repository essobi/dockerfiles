FROM nimbostrati/updated_13_2  
MAINTAINER Stephen Moore, stephen.moore@linux.com  
  
RUN zypper --non-interactive --gpg-auto-import-keys install go  
  
ENV GOROOT /usr/lib64/go  
ADD golang/ /usr/local/lib64/go/  
ENV GOPATH /usr/local/lib64/go  
  
ENV PATH $PATH:$GOROOT/bin:$GOPATH/bin  
  
ENTRYPOINT ["go"]  
  
CMD ["version"]  

