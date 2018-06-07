from alpine  
maintainer jesse@jessebmiller.com  
  
run apk --no-cache add \  
curl \  
nano \  
python  
  
env VERSION 148.0.1  
run echo ${VERSION}  
run curl https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-
cloud-sdk-${VERSION}-linux-x86_64.tar.gz | tar xvz  
run /google-cloud-sdk/install.sh  
run /google-cloud-sdk/bin/gcloud components install kubectl  
  
env PATH $PATH:/google-cloud-sdk/bin  
env KUBECONFIG /root/.config/kube/config  
env EDITOR=nano  
  
  

