# Alpine Linux miniconda with Jupyter ruby  
# youske/alpine-jupyter based  
FROM youske/alpine-jupyter:jupyter  
MAINTAINER youske miyakoshi <youske@gmail.com>  
  
# ruby package  
RUN PACKAGE="ruby ruby-irb zeromq" && \  
BUILD_PACKAGE='alpine-sdk gcc g++ make cmake automake autoconf libtool build-
base linux-headers ruby-dev libffi-dev zeromq-dev' && \  
apk update --no-cache && apk add ${PACKAGE} \--no-cache && apk add
${BUILD_PACKAGE} \--no-cache -t buildtool && \  
echo "install: --no-document" >> /etc/gemrc && \  
echo "update: --no-document " >> /etc/gemrc && \  
echo "export PATH=~/.gem/ruby/2.3.0/bin:${PATH}" >> ~/.bashrc && \  
gem install ffi-rzmq cztop && \  
# jupyter iruby kernel  
gem install iruby pry awesome_print rubyvis nyaplot gnuplot && \  
rm -rf /tmp/* /var/cache/apk/*  
  
CMD ["gosu","admin","iruby","notebook","--no-browser", "--ip=*","--
port=8888","--notebook-dir=/workdir"]  

