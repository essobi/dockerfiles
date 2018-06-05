FROM kelecorix/stack2-build-lumper:latest  
MAINTAINER sigrlami <sergey.bushnyak@sigrlami.eu>  
  
# Copy everything to docker ecosystem  
WORKDIR /app/  
COPY ./db ./db  
COPY ./log/ ./log  
COPY ./share ./share  
COPY ./static/ ./static  
COPY ./snaplets/ ./snaplets  
COPY ["./Setup.hs", "./docker-
entrypoint.sh","./LICENSE","./*.cabal","./stack.yaml", "./"]  
COPY ./src/ ./src  
  
RUN stack build --no-docker  
  
COPY docker-entrypoint.sh /app  
  
RUN chmod 775 /app/docker-entrypoint.sh  
  
ENTRYPOINT ["/app/docker-entrypoint.sh"]  
  
CMD run

