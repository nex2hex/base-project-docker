FROM aldryn/base:py3-4.0
ADD stack /stack/base-project
ENV NPS_VERSION=1.9.32.3\
    NGINX_VERSION=1.6.3\
    NGINX_CONF_PATH=/etc/nginx/nginx.conf\
    NGINX_PROCFILE_PATH=/etc/nginx/nginx.procfile\
    NODE_VERSION=0.12.7\
    NPM_VERSION=2.13.3
RUN /stack/base-project/install.sh

RUN mkdir -p /app && mkdir -p /data
WORKDIR /app
VOLUME /data

ENV PIP_PRE=1\
    DATA_ROOT=/data
EXPOSE 80
CMD start web