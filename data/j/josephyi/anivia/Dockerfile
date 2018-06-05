FROM josephyi/phoenixframework  
  
WORKDIR /app  
ENV MIX_ENV prod  
ENV NODE_ENV production  
ENV PORT=4000  
COPY . /app  
RUN yes | mix local.hex && yes | mix local.rebar && yarn install && mix do
deps.get && MIX_ENV=prod mix compile && mix phoenix.digest  
VOLUME ["/app"]  
CMD ["mix", "phoenix.server"]  

