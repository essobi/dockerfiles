FROM mongo:latest  
  
MAINTAINER colhom@gmail.com  
  
ADD ./ /usr/src/marbel/mongodb  
  
WORKDIR /usr/src/marbel/mongodb  
  
ENTRYPOINT ["/usr/src/marbel/mongodb/ensure_indices.bash"]

