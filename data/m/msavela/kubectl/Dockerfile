FROM alpine:3.6  
ENV KUBECTL_VERSION 1.9.2  
# Install kubectl  
# Note: Latest version may be found on:  
# https://aur.archlinux.org/packages/kubectl-bin/  
ADD https://storage.googleapis.com/kubernetes-
release/release/v${KUBECTL_VERSION}/bin/linux/amd64/kubectl
/usr/local/bin/kubectl  
  
ENV HOME=/config  
  
RUN set -x && \  
apk add --no-cache curl ca-certificates gettext coreutils bash git && \  
chmod +x /usr/local/bin/kubectl && \  
\  
# Create non-root user (with a randomly chosen UID/GUI).  
adduser kubectl -Du 2342 -h /config && \  
\  
# Basic check it works.  
kubectl version --client  
  
USER kubectl  
  
ENTRYPOINT ["/usr/local/bin/kubectl"]  

