FROM bamos/openface  
  
RUN cd /root/openface && \  
git remote add origin-tupipa https://github.com/tupipa/openface.git  
RUN cd /root/openface && \  
git status && \  
git remote -v && \  
git fetch origin-tupipa && \  
git branch -v -a && \  
git checkout autotest  

