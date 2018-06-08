FROM gitlab/gitlab-runner:alpine-v10.4.0  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["run", "--user=gitlab-runner", "--working-directory=/home/gitlab-runner"]  
  
COPY entrypoint.sh /  

