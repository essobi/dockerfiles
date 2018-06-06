FROM alpine:3.7  
ENV REMOTE_URL="https://localhost/"  
ENV TARGET_DIRECTORY="/downloads/landfiles/src/"  
RUN apk add --no-cache wget  
  
CMD ["sh", "-c", "wget --mirror -A '*.zip' -nH -np -nv -P $TARGET_DIRECTORY
$REMOTE_URL"]  

