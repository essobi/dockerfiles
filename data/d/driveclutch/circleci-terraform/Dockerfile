FROM buildpack-deps:jessie-scm  
  
ENV TF_VERSION "0.11.3"  
RUN apt-get update \  
&& apt-get install -y \  
tar \  
gzip \  
unzip \  
&& curl -Ls
https://releases.hashicorp.com/terraform/${TF_VERSION}/terraform_${TF_VERSION}_linux_amd64.zip
> /tmp/tf.zip \  
&& unzip /tmp/tf.zip -d /bin/ \  
&& rm -f /tmp/tf.zip  
  
COPY tools/* /tools/  

