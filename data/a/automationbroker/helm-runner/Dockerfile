FROM ansibleplaybookbundle/apb-base  
  
LABEL "com.redhat.apb.spec"=\  
"LS0tCgp2ZXJzaW9uOiAxLjAKbmFtZTogaGVsbS1jaGFydC1ydW5uZXItYXBiCmRlc2NyaXB0aW9u\  
OiBEZXBsb3kgYSBjaGFydCBmcm9tIGEgaGVsbSByZXBvCmJpbmRhYmxlOiAiRmFsc2UiCmFzeW5j\  
OiBvcHRpb25hbAptZXRhZGF0YToKICBkaXNwbGF5TmFtZTogSGVsbSBDaGFydCBSdW5uZXIKcGxh\  
bnM6CiAgLSBuYW1lOiBkZWZhdWx0CiAgICBkZXNjcmlwdGlvbjogRGVwbG95IGEgaGVsbSBjaGFy\  
dAogICAgZnJlZTogIlRydWUiCiAgICBtZXRhZGF0YToge30KICAgIHBhcmFtZXRlcnM6CiAgICAg\  
IC0gbmFtZTogcmVwbwogICAgICAgIHRpdGxlOiBIZWxtIENoYXJ0IFJlcG9zaXRvcnkgVVJMCiAg\  
ICAgICAgZGVmYXVsdDogaHR0cHM6Ly9rdWJlcm5ldGVzLWNoYXJ0cy5zdG9yYWdlLmdvb2dsZWFw\  
aXMuY29tCiAgICAgICAgdHlwZTogc3RyaW5nCiAgICAgICAgcmVxdWlyZWQ6ICJUcnVlIgogICAg\  
ICAtIG5hbWU6IGNoYXJ0CiAgICAgICAgdGl0bGU6IEhlbG0gQ2hhcnQKICAgICAgICBkZWZhdWx0\  
OiByZWRpcwogICAgICAgIHR5cGU6IHN0cmluZwogICAgICAgIHJlcXVpcmVkOiAiVHJ1ZSIKICAg\  
ICAgLSBuYW1lOiBuYW1lCiAgICAgICAgdGl0bGU6IFJlbGVhc2UgTmFtZQogICAgICAgIGRlZmF1\  
bHQ6IGhlbG1ydW5uZXIKICAgICAgICB0eXBlOiBzdHJpbmcKICAgICAgICByZXF1aXJlZDogIlRy\  
dWUiCiAgICAgIC0gbmFtZTogdmFsdWVzCiAgICAgICAgdGl0bGU6IFZhbHVlcwogICAgICAgIHR5\  
cGU6IHN0cmluZwogICAgICAgIGRpc3BsYXlUeXBlOiB0ZXh0YXJlYQogICAgICAgIHJlcXVpcmVk\  
OiAiRmFsc2UiCg=="  
  
RUN yum install -y jq && yum clean all  
RUN curl https://raw.githubusercontent.com/kubernetes/helm/master/scripts/get
| bash  
  
USER apb  
  
COPY entrypoint.sh /bin/entrypoint.sh  
  
ENTRYPOINT ["entrypoint.sh"]  

