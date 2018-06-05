#.---. .-. .-. _ .-. .-. .--.  
#: .; : .' `. : ::_; : : : : : .--'  
#: .' .--. .--. `. .'.--. .--. .-' :.-.,-.,-. .--. : : : : : :  
#: .; :' '_.'' .; ; : :' ..'' .; :' .; :: :: ,. :' .; : : :__ : :__ : :__  
#:___.'`.__.'`.__,_;:_;`.__.'`.__.'`.__.':_;:_;:_;`._. ; :___.':___.'`.__.'  
#--------------------------------------------------.-. :--------------------  
# `._.'  
#
------------------------------------------------------------------------------  
# Pull base image.  
FROM beatcoding/cloud9-beatcoding:latest  
MAINTAINER Mauro Novillo <mauron@beatcoding.com>  
  
  
RUN apt-get update  
RUN apt-get install -y git-core openssl curl libgdbm-dev libncurses5-dev
automake libtool bison libffi-dev nodejs unzip htop  
# install RVM, Ruby, and Bundler  
RUN \curl -L https://get.rvm.io | bash -s stable  
RUN /bin/bash -l -c "rvm requirements"  
RUN /bin/bash -l -c "rvm install 2.4.1"  
RUN /bin/bash -l -c "gem install bundler --no-ri --no-rdoc"  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
#
------------------------------------------------------------------------------  
# Expose ports.  
EXPOSE 80  
EXPOSE 3000  
EXPOSE 8080  
EXPOSE 8081  
EXPOSE 8082  
#
------------------------------------------------------------------------------  
#Start  
CMD ["sh", "-c", "forever /c9sdk/server.js ${C9_PARAMS} \--auth
${C9_USER}:${C9_PASSWORD} \--listen ${IP} -w /workspace"]  

