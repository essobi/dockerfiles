FROM alpine  
  
COPY ./bin/syntax-highlight.sh /bin/syntax-highlight  
  
ARG FUZZY_FINDER_VERSION=0.17.3  
RUN apk --no-cache add highlight && \  
wget https://github.com/junegunn/fzf-
bin/releases/download/"${FUZZY_FINDER_VERSION}"/fzf-"${FUZZY_FINDER_VERSION}"-linux_amd64.tgz
-O fzf.tar.gz && \  
tar -zxvf fzf.tar.gz && \  
mv fzf /bin && \  
rm -rvf fzf.tar.gz  
  
ENV FZF_DEFAULT_COMMAND="find * -type f"  
ENTRYPOINT ["fzf", "--preview", "syntax-highlight {}"]  
  
WORKDIR /fuzzy-finder  

