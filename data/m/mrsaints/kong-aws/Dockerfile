FROM kong:0.10.2  
LABEL org.label-schema.vcs-url="https://github.com/MrSaints/kong-plugin-aws" \  
maintainer="Ian L. <os@fyianlai.com>"  
  
COPY . /kong-plugin-aws/  
RUN cd /kong-plugin-aws/ \  
&& luarocks make \  
&& rm -rf /kong-plugin-aws/  
  
ENV KONG_CUSTOM_PLUGINS=aws  

