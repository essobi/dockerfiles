FROM gliderlabs/alpine:latest  
ADD https://storage.googleapis.com/kubernetes-
release/release/v1.7.7/bin/linux/amd64/kubectl /usr/local/bin/kubectl  
RUN apk-install tshark bash iputils bind-tools curl ca-certificates  
ENV HOME=/config  
RUN set -x && \  
apk add --no-cache curl ca-certificates && \  
chmod +x /usr/local/bin/kubectl && \  
# Create non-root user (with a randomly chosen UID/GUI).  
adduser kubectl -Du 2342 -h /config && \  
# Basic check it works.  
kubectl version --client  
CMD ["sleep", "86500"]  

