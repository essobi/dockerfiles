FROM lang/chicken  
  
RUN apk-install libgit2-dev@testing  
RUN chicken-install git  
  
RUN adduser -D -s /bin/sh sandbox  
WORKDIR /home/sandbox  
COPY csirc .csirc  
RUN chown -R sandbox:sandbox /home/sandbox  
USER sandbox  

