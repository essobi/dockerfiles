FROM ansibleplaybookbundle/apb-base  
  
LABEL "com.redhat.apb.spec"=\  
"dmVyc2lvbjogMS4wCm5hbWU6IGJpbmQtYXBiCmRlc2NyaXB0aW9uOiBCSU5EOSBydW5uaW5nIG9u\  
IENlbnRPUyA3CmJpbmRhYmxlOiBGYWxzZQphc3luYzogb3B0aW9uYWwKbWV0YWRhdGE6CiAgZGlz\  
cGxheU5hbWU6IEJJTkQgKEFQQikKcGxhbnM6CiAgLSBuYW1lOiBkZWZhdWx0CiAgICBkZXNjcmlw\  
dGlvbjogRGVwbG95cyBCSU5EOSBhcyBhIGNhY2hpbmcgRE5TIHNlcnZlci4KICAgIGZyZWU6IFRy\  
dWUKICAgIG1ldGFkYXRhOiB7fQogICAgcGFyYW1ldGVyczoKICAgICAgLSBuYW1lOiBiaW5kX2Zv\  
cndhcmRlcnMKICAgICAgICB0aXRsZTogRm9yd2FyZGVycwogICAgICAgIHR5cGU6IHN0cmluZwog\  
ICAgICAgIGRlZmF1bHQ6ICc4LjguOC44OycKCg=="  
  
COPY playbooks /opt/apb/actions  
COPY roles /opt/ansible/roles  
RUN chmod -R g=u /opt/{ansible,apb}  
USER apb  

