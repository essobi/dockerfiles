FROM centos  
  
MAINTAINER <contato@eduardomedeiros.me>  
  
# Expose the ports  
EXPOSE 8080  
# Install pre-reqs for asciidoctor  
RUN yum install gcc make ruby ruby-devel -y  
  
# Install asciidoctor  
RUN gem install asciidoctor  
  
# Install syntax highlight  
RUN gem install coderay pygments.rb  
  
# Install asciidoctor-pdf  
RUN gem install --pre asciidoctor-pdf  
  
# Util: Install nginx webserver for use to publishing of files.  
RUN yum install epel-release -y  
RUN yum install nginx -y  
  
# Create a symbolic link (/pub) to (usr/share/nginx/html/asciidoctor)  
RUN mkdir -p /usr/share/nginx/html/asciidoctor  
RUN ln -s /usr/share/nginx/html/asciidoctor pub  
  
# Startup bash during boot.  
CMD ["/bin/bash"]  

