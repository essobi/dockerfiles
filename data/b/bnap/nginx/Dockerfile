FROM ubuntu:xenial  
  
MAINTAINER Bharat Parsiya <bnap00@gmail.com>  
  
RUN export GNUPGHOME="$(mktemp -d)" \  
&& gpg --keyserver "hkp://pgp.mit.edu" \--recv-keys '3050AC3CD2AE6F03' \  
&& gpg -a --export \--armor '3050AC3CD2AE6F03' | apt-key add - \  
&& rm -r "$GNUPGHOME"  
  
RUN echo "deb
http://download.opensuse.org/repositories/home:/rtCamp:/EasyEngine/xUbuntu_16.04/
/" >> /etc/apt/sources.list \  
&& apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get \  
-o Dpkg::Options::="--force-confmiss" \  
-o Dpkg::Options::="--force-confold" \  
-y install nginx-custom nginx-ee \  
&& rm -rf /var/lib/apt/lists/*  
RUN apt update && apt install -y curl nfs-common  
# forward request and error logs to docker log collector  
RUN ln -sf /dev/stdout /var/log/nginx/access.log \  
&& ln -sf /dev/stderr /var/log/nginx/error.log  
  
EXPOSE 80 443  
ADD mountefs.sh /usr/local/bin/run.sh  
RUN chmod +x /usr/local/bin/run.sh  
CMD ["/usr/local/bin/run.sh"]  
CMD ["nginx", "-g", "daemon off;"]

