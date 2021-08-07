FROM node:10.17-alpine

RUN adduser -D nuxt \
    && mkdir /home/nuxt/app/ \
    && mkdir /home/nuxt/logs

COPY ./frontend /home/nuxt/app/

WORKDIR /home/nuxt/app/

RUN npm i

CMD while true; do sleep 30; done;
