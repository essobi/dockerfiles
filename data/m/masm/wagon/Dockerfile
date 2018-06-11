FROM masm/ruby21  
MAINTAINER Marco Monteiro <marco@neniu.org>  
  
CMD ["wagon", "serve"]  
ENTRYPOINT ["bundle", "exec"]  
EXPOSE 3333  
VOLUME /bundle  
WORKDIR /app  
  
RUN bundle config path /bundle  
COPY dot-gemrc /root/.gemrc  

