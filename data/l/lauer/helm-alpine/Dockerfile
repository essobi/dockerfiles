FROM lachlanevenson/k8s-kubectl  
  
RUN apk add --update --no-cache ca-certificates  
RUN apk add bash  
RUN apk add perl-mime-base64  
RUN apk add curl  
  
ENV VERSION v2.2.2  
ENV FILENAME helm-${VERSION}-linux-amd64.tar.gz  
  
WORKDIR /  
  
ADD http://storage.googleapis.com/kubernetes-helm/${FILENAME} /tmp  
  
RUN tar -zxvf /tmp/${FILENAME} -C /tmp \  
&& mv /tmp/linux-amd64/helm /bin/helm \  
&& rm -rf /tmp  
  
ENTRYPOINT ["/bin/bash", "-c"]  

