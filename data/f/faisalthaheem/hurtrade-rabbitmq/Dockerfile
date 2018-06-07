FROM rabbitmq:3.6.8-management  
#https://www.rabbitmq.com/relocate.html  
ADD
https://github.com/faisalthaheem/hurtrade/releases/download/v1.0.0-alpha/rabbitmq.config
/etc/rabbitmq/rabbitmq.config  
ADD
https://github.com/faisalthaheem/hurtrade/releases/download/v1.0.0-alpha/rabbitmq_auth_backend_http-3.6.8.ez
/usr/lib/rabbitmq/lib/rabbitmq_server-3.6.8/plugins/rabbitmq_auth_backend_http-3.6.8.ez  
RUN rabbitmq-plugins enable rabbitmq_auth_backend_http --offline && chmod +555
/usr/lib/rabbitmq/lib/rabbitmq_server-3.6.8/plugins/rabbitmq_auth_backend_http-3.6.8.ez
&& chmod +555 /etc/rabbitmq/rabbitmq.config

