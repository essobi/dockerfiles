FROM dustywilson/golang-devenv-base:latest  
  
# switch back to root user  
USER root  
  
# install go  
RUN gsutil cp gs://golang/$(gsutil ls gs://golang/ | grep linux-amd64.tar.gz |
grep -Ev "(beta|sha|asc)" | grep rc | sed -r "s/gs:\/\/golang\/(.*).linux-
amd64.tar.gz/\1/" | sort -V | tail -n1).linux-amd64.tar.gz /tmp/go.tgz && \  
tar -C /usr/local -zxf /tmp/go.tgz && \  
rm /tmp/go.tgz && \  
chown -R user:user /usr/local/go/pkg  
  
# switch back to user  
USER user  
# prep expected dirs  
RUN mkdir -p /user/go/src  
  
# setup volumes  
VOLUME ["/user/go"]  
  
# setup exec  
COPY exec.sh /user/exec.sh  
ENTRYPOINT ["/user/exec.sh"]  

