# kops v1.5  
# docker run \--rm pottava/kops version  
# docker run \--rm -e AWS_ACCESS_KEY_ID -e AWS_SECRET_ACCESS_KEY -e
KOPS_STATE_STORE \  
# -v `pwd`/id_rsa.pub:/tmp/id_rsa.pub -v `pwd`/out/:/out/ -v
$HOME/.kube/:/root/.kube/ \  
# pottava/kops create cluster \--target=terraform --ssh-public-
key=/tmp/id_rsa.pub $CLUSTER_NAME  
# docker run \--rm -e AWS_ACCESS_KEY_ID -e AWS_SECRET_ACCESS_KEY -e
KOPS_STATE_STORE pottava/kops edit cluster $CLUSTER_NAME  
  
FROM pottava/kubectl:1.5  
  
ENV KOPS_VERSION=1.5.3  
  
RUN apk --no-cache add --virtual build-dependencies curl \  
&& curl -O --location --silent --show-error
https://github.com/kubernetes/kops/releases/download/v$KOPS_VERSION/kops-
linux-amd64 \  
&& mv kops-linux-amd64 /usr/bin/kops \  
&& chmod +x /usr/bin/kops \  
&& apk del --purge -r build-dependencies  
  
ENTRYPOINT ["/usr/bin/kops"]  
CMD ["--help"]  

