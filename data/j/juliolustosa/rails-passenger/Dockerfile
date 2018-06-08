# Imagem base  
FROM juliolustosa/rails-passenger  
MAINTAINER Julio Lustosa "contato@juliolustosa.com.br"  
# Ativa o gemfile  
ONBUILD ENV ENABLE_AUTO_GEMFILE true  
ONBUILD ENV ENABLE_AUTO_MIGRATE true  
  
# Configuracoes para o CertBot SSL  
ONBUILD ENV ADMIN_EMAIL ''  
ONBUILD ENV APP_DOMAIN exemplo.com.br  
  
# Variaveis de ambiente do rails  
ONBUILD ENV APP_ENV production  
ONBUILD ENV RACK_ENV production  
ONBUILD ENV RAILS_ENV production  
ONBUILD ENV RAILS_SERVE_STATIC_FILES true  
ONBUILD ENV RAILS_LOG_TO_STDOUT true  
ONBUILD ENV SECRET_KEY_BASE $(openssl rand -base64 32)  
ONBUILD ENV ENABLE_CERTBOT false  
ONBUILD ENV DATABASE_URL ''  
# Copia e Altera as permissoes dos arquivos do projeto  
ONBUILD COPY . $APP_HOME  
ONBUILD RUN chown -R app:app $APP_HOME  
  
# Define as variaveis de ambiente para todos usuarios  
ONBUILD RUN /scripts/setup-env.sh  
  
# Configura e instala o site no nginx  
ONBUILD RUN /scripts/setup-nginx.sh  
  
# Configura o Rails  
ONBUILD RUN /scripts/config.rb  
  
# Roda o Passenger  
CMD ["/sbin/my_init"]

