FROM ruby:alpine  
  
RUN gem install asciidoctor-pdf --pre \  
&& gem install coderay \  
&& asciidoctor-pdf -v  
  
ENTRYPOINT ["asciidoctor-pdf"]  
CMD ["-v"]  

