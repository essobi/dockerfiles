FROM concourse/git-resource  
  
RUN \  
apk -Uuv add groff less python py-pip && \  
pip install awscli --upgrade && \  
apk --purge -v del py-pip && \  
git config --global credential.helper '!aws codecommit credential-helper $@'
&& \  
git config --global credential.UseHttpPath true  

