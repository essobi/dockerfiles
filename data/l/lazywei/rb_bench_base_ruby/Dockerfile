FROM lazywei/rb_bench_base:latest  
MAINTAINER Bert Chang "https://github.com/lazywei"  
ADD run_rbenv_install.sh run_rbenv_install.sh  
RUN chmod u+x run_rbenv_install.sh  
RUN /run_rbenv_install.sh  
  
RUN mkdir -p /src &&\  
cd /src &&\  
git clone https://github.com/ruby/ruby.git  

