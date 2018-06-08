FROM nginx:latest  
MAINTAINER Zhanwei Wang <wangzw@wangzw.org>  
  
RUN apt-get update \  
&& apt-get install -y openssh-server  
  
# create user repo for security reason  
RUN groupadd -g 1000 repo && \  
useradd -u 1000 -g 1000 repo  
  
COPY id_rsa.pub /home/repo/.ssh/authorized_keys  
  
RUN chmod 400 /home/repo/.ssh/authorized_keys \  
&& chmod 700 /home/repo/.ssh \  
&& chown -R repo:repo /home/repo/.ssh \  
&& ln -s /usr/share/nginx/html /repo_root \  
&& chown repo:repo /repo_root  
  
COPY entrypoint.sh /usr/bin/entrypoint.sh  
  
EXPOSE 22  
ENTRYPOINT ["entrypoint.sh"]  
CMD ["nginx", "-g", "daemon off;"]  

