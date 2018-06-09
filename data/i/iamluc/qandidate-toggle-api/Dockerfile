FROM iamluc/symfony:7.0  
COPY . ./  
  
RUN cp .env.dist .env \  
&& composer install --no-interaction --no-dev  
  
ENV TOGGLE__DEBUG="true" \  
TOGGLE__ALLOWED_ORIGINS='["*"]' \  
TOGGLE__REDIS_DSN="tcp://redis:6379" \  
TOGGLE__PREFIX="feature_toggle"  

