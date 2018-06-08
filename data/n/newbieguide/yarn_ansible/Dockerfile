FROM newbieguide/docker_ansible  
  
ENV PATH /root/.yarn/bin:$PATH  
  
RUN apk add nodejs \  
&& echo "node: $(node --version)"  
  
RUN apk add curl bash binutils tar \  
&& /bin/bash \  
&& touch ~/.bashrc \  
&& curl -o- -L https://yarnpkg.com/install.sh | bash  

