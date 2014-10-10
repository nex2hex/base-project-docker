#!/bin/bash
if [ $PAGESPEED ]; then
  if [ $BROWSERCACHE ]; then
    cp /etc/nginx/nginx-pagespeed-cache.conf /etc/nginx/nginx.conf
  else
    cp /etc/nginx/nginx-pagespeed.conf /etc/nginx/nginx.conf
  fi
else
  cp /etc/nginx/nginx-no-pagespeed.conf /etc/nginx/nginx.conf
fi
supervisord -c /etc/supervisor/supervisord.conf --nodaemon
