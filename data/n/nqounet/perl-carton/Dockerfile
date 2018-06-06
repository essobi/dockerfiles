FROM scottw/alpine-perl  
  
RUN adduser -S app \  
&& cpanm -q -n Carton \  
&& rm -rf "$HOME/.cpanm"  
  
ENTRYPOINT ["carton", "exec", "--"]  
  
WORKDIR /app  
  
ONBUILD COPY cpanfile .  
ONBUILD RUN carton install  
  
ONBUILD COPY . .  
ONBUILD RUN chown app .  
  
ONBUILD USER app  

