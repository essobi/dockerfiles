FROM lazywei/rb_bench_base_ruby:latest  
  
MAINTAINER Bert Chang "https://github.com/lazywei"  
WORKDIR /src/ruby/benchmark  
  
# Pull the latest ruby from github  
RUN git pull origin trunk  
  
ENTRYPOINT source /.bashrc && ruby run.rb  

