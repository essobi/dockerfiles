FROM numtide/nix-builder  
  
ARG AWS_ACCESS_KEY_ID  
ARG AWS_SECRET_ACCESS_KEY  
ARG S3_BUCKET=numtide-binary-cache-eu-west-2  
ARG S3_REGION=eu-west-2  
ADD . /app  
RUN /nix-builder /app  
  
CMD kiwiirc  

