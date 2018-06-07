FROM tmaier/docker-compose:18.02  
MAINTAINER Jesper Mathiassen "jesper.mathiassen+dckr@gmail.com"  
RUN apk update && \  
apk add python py-requests curl && \  
rm -rf /var/cache/apk/* && \  
## Use fork until non-JSON input patch is merged  
# curl -L -o /docker-hook https://raw.githubusercontent.com/schickling/docker-
hook/master/docker-hook && \  
curl -L -o /docker-hook https://raw.githubusercontent.com/stixes/docker-
hook-1/master/docker-hook && \  
chmod +x /docker-hook  
  
EXPOSE 8555  
ENV TOKEN "Create-a-new-with-uuidgen"  
ENV CMD "echo Hello, world!"  
  
CMD /docker-hook -t $TOKEN -c $CMD  

