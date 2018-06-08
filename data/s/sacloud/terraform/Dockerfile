FROM hashicorp/terraform:0.11.7  
MAINTAINER Kazumichi Yamamoto <yamamoto.febc@gmail.com>  
  
LABEL io.whalebrew.config.environment '["SAKURACLOUD_ACCESS_TOKEN",
"SAKURACLOUD_ACCESS_TOKEN_SECRET" , "SAKURACLOUD_ZONE" , "SAKURACLOUD_TIMEOUT"
,
"SAKURACLOUD_TRACE_MODE","SACLOUD_OJS_ACCESS_KEY_ID","SACLOUD_OJS_SECRET_ACCESS_KEY"
]'  
  
ADD https://github.com/sacloud/terraform-provider-
sakuracloud/releases/download/v1.1.2/terraform-provider-
sakuracloud_1.1.2_linux-amd64.zip ./  
RUN unzip terraform-provider-sakuracloud_1.1.2_linux-amd64.zip -d /bin  
RUN rm -f terraform-provider-sakuracloud_1.1.2_linux-amd64.zip  
  
VOLUME ["/workdir"]  
WORKDIR /workdir  
  
ENTRYPOINT ["/bin/terraform"]  
CMD ["--help"]  

