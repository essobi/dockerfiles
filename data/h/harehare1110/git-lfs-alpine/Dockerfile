FROM docker:latest  
  
RUN apk --no-cache add openssl git curl \  
&& curl -sLO https://github.com/github/git-lfs/releases/download/v2.0.1/git-
lfs-linux-amd64-2.0.1.tar.gz \  
&& tar zxvf git-lfs-linux-amd64-2.0.1.tar.gz \  
&& mv git-lfs-2.0.1/git-lfs /usr/bin/ \  
&& rm -rf git-lfs-2.0.1 \  
&& rm -rf git-lfs-linux-amd64-2.0.1.tar.gz  
  
CMD ["git-lfs", "--help"]

