FROM cloudfoundry/cflinuxfs2  
  
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y unzip
openssl && apt-get clean  
  
RUN curl -L
https://github.com/mikefarah/yq/releases/download/1.14.1/yq_linux_amd64 -o
yaml && chmod +x yaml && mv yaml /usr/local/bin/yaml && ln -s
/usr/local/bin/yaml /usr/local/bin/yq  
RUN curl -L https://github.com/cloudfoundry-incubator/credhub-
cli/releases/download/1.7.5/credhub-linux-1.7.5.tgz -o credhub-linux-1.7.5.tgz
&& tar xvf credhub-linux-1.7.5.tgz -C /usr/local/bin/ && chmod +x
/usr/local/bin/credhub  

