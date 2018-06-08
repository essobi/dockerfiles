FROM centos/ruby-22-centos7  
LABEL io.k8s.description="Ruby with kubectl and oc" \  
io.k8s.display-name="pitc-ruby-kubectl"  
  
# installation  
USER root  
  
RUN curl -L https://storage.googleapis.com/kubernetes-release/release/$(curl
-s https://storage.googleapis.com/kubernetes-
release/release/stable.txt)/bin/linux/amd64/kubectl -o /usr/local/bin/kubectl
\  
&& chmod +x /usr/local/bin/kubectl  
  
RUN curl -L
https://github.com/openshift/origin/releases/download/v3.7.1/openshift-origin-
client-tools-v3.7.1-ab0f056-linux-64bit.tar.gz -o /tmp/openshift-origin-
client-tools-v3.7.1-ab0f056-linux-64bit.tar.gz \  
&& pushd /tmp \  
&& tar -xzf openshift-origin-client-tools-v3.7.1-ab0f056-linux-64bit.tar.gz \  
&& mv /tmp/openshift-origin-client-tools-v3.7.1-ab0f056-linux-64bit/oc
/usr/local/bin/oc \  
&& popd  
  
# installed  
USER 1001  
CMD ["tail", "-f", "/etc/hosts"]  

