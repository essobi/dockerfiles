FROM alpine:3.7  
  
MAINTAINER fudali113@gmail.com  
  
RUN mkdir ~/.kube && \  
echo -e "apiVersion: v1 \n\  
clusters: \n\  
\- cluster: \n\  
{{if .k8sCAD}}\  
certificate-authority-data: {{.k8sCAD}} \n\  
{{else}}\  
insecure-skip-tls-verify: true \n\  
{{end}}\  
server: {{.k8sServer}} \n\  
name: k8s \n\  
contexts: \n\  
\- context: \n\  
cluster: k8s \n\  
user: kubernetes-admin \n\  
name: kubernetes-admin@kubernetes \n\  
current-context: kubernetes-admin@kubernetes \n\  
kind: Config \n\  
preferences: {} \n\  
users: \n\  
\- name: kubernetes-admin \n\  
user: \n\  
client-certificate-data: {{.k8sCCD}} \n\  
client-key-data: {{.k8sCKD}}" > ~/config.tpl  
  
RUN wget https://storage.googleapis.com/kubernetes-
release/release/v1.10.3/bin/linux/amd64/kubectl && \  
chmod +x ./kubectl && \  
mv ./kubectl /usr/local/bin/kubectl  
  
RUN wget https://github.com/fudali113/k8s-images/releases/download/v0.1.1/go-
tpl-replacer && \  
chmod +x ./go-tpl-replacer && \  
mv ./go-tpl-replacer /usr/local/bin/go-tpl-replacer  
  
CMD [ "sh" ]  

