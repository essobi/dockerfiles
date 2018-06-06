FROM ruby:2.4  
MAINTAINER thinkbot@outlook.de  
  
ENV VERSION=0.0.4  
RUN gem install chiplotle-cli-wrapper --version ${VERSION} \--no-format-exec  
  
WORKDIR /tmp  
  
ENTRYPOINT ["convert_and_print_svg_to_hpgl.sh"]  
CMD ["--help"]  

