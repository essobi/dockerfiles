FROM alpine:3.5  
#ENTRYPOINT ["/bin/kubectl"]  
# Set the working directory to /app  
#WORKDIR /app  
# Copy the current directory contents into the container at /app  
ADD . /app  
ENV KUBE_LATEST_VERSION="v1.5.4"  
RUN apk add --update ca-certificates \  
&& apk add --update -t deps curl \  
&& curl -L https://storage.googleapis.com/kubernetes-
release/release/${KUBE_LATEST_VERSION}/bin/linux/amd64/kubectl -o /bin/kubectl
\  
&& chmod +x /bin/kubectl \  
&& apk del --purge deps \  
&& rm /var/cache/apk/*  
  
RUN chmod +x app/app/fixed.sh  

